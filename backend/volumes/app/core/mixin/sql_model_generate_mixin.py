from sqlmodel import SQLModel


class SQLModelGenerateMixin:

    __config__ = {}

    @classmethod
    def generate_by(
        cls: type["SQLModelGenerateMixin"],
        generate_from: SQLModel,
        exclude_unset: bool = True,
        **kwargs,
    ) -> "SQLModelGenerateMixin":
        return cls(**generate_from.dict(
            exclude_unset=exclude_unset,
            **kwargs,
        ))
