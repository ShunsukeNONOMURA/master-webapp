# class IUserRepository(ABCMeta):
#     # @abstractmethod
#     # def __init__(self, db: Session) -> None:
#     #     pass

#     # @abstractmethod
#     # def _fetch_by_id(self, user_id: StudentIdValueObject) -> StudentModel | None:
#     #     pass

#     # @abstractmethod
#     # def _apply(self, model: StudentModel) -> StudentModel:
#     #     pass

#     @abstractmethod
#     def find_by_id(self, user_id: User.UserId) -> User:
#         pass

#     @abstractmethod
#     def insert(self, user: User):
#         pass

#     # @abstractmethod
#     # def update(self, user: User) -> StudentModel:
#     #     pass

#     @abstractmethod
#     def delete(self, user_id: User.UserId):
#         pass

#     # @abstractmethod
#     # def refresh_to_entity(self, model: StudentModel) -> User:
#     #     pass