from abc import ABCMeta

from sqlmodel import SQLModel


class BaseInputDTO(SQLModel, metaclass=ABCMeta):
    """UseCaseのBaseInputDTOベース."""
