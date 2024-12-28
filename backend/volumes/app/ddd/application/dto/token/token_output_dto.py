

from app.core.base import BaseOutputDTO
from app.ddd.domain import Token


class CreateTokenOutputDTO(BaseOutputDTO, Token):
    pass

