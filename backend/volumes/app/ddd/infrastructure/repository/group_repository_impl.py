# class ErrorCode:

from sqlmodel import Session, select

from app.ddd.domain import (
    Group,
    GroupDuplicationError,
    GroupId,
    GroupNotFoundError,
    GroupRepository,
    GroupUpdateConflictError,
)
from migrations.models import TGroup


class GroupRepositoryImpl(GroupRepository):
    def __init__(self, session: Session) -> None:
        self.__session: Session = session

    def _fetch_by_id(self, _id: str) -> TGroup | None:
        statement = select(TGroup).where(TGroup.group_id == _id)
        return self.__session.exec(statement).first()

    def _apply(self, model: TGroup) -> None:
        self.__session.add(model)

    def _delete(self, model: TGroup) -> None:
        self.__session.delete(model)

    def find_by_id(self, _id: GroupId) -> Group:
        model: TGroup | None = self._fetch_by_id(_id.root)
        if model is None:
            raise GroupNotFoundError(_id.root)
        return Group.model_validate(model)

    def insert(self, group: Group) -> None:
        model: TGroup | None = self._fetch_by_id(group.group_id)
        if model is not None: # 重複判定
            raise GroupDuplicationError(group.group_id)
        model = TGroup.model_validate(group.model_dump(exclude={"created_at", "updated_at"})) # 新規作成
        self._apply(model)


    def update(self, group: Group) -> None:
        model: TGroup | None = self._fetch_by_id(group.group_id)
        if model is None: # ない場合更新できない 現在のユースケースでは基本的に発生しない
            raise GroupNotFoundError(group.group_id)
        if group.updated_at != model.updated_at: # 更新日検証による楽観的ロックの確認
            raise GroupUpdateConflictError(group_id=group.group_id)
        model.sqlmodel_update(group.model_dump(exclude={"created_at", "updated_at", "group_reports"})) # 更新データの統合
        self._apply(model)

    def delete(self, _id: GroupId) -> None:
        model: TGroup | None = self._fetch_by_id(_id.root)
        if model is None:
            raise GroupNotFoundError(_id.root)

        # TODO(nonomura): 論理削除する場合
        # model.updated_at = datetime.now()
        # model.deleted_at = datetime.now() # 論理削除する場合
        # self._apply(model)

        self._delete(model) # 物理削除用

    def query(self) -> list[Group]:
        """TODO(nonomura): 検索条件整理後に整理。必要に応じてクエリサービスに分ける."""
        models: list[TGroup] = self.__session.query(TGroup).all()
        return [Group.model_validate(model) for model in models]

