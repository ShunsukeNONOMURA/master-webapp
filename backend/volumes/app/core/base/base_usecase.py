from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING, Generic, TypeVar

if TYPE_CHECKING:
    from .base_input_dto import BaseInputDTO
    from .base_output_dto import BaseOutputDTO

# TypeVarsを定義
BaseInputDTOType = TypeVar("BaseInputDTOType", bound="BaseInputDTO", default="BaseInputDTO")
BaseOutputDTOType = TypeVar("BaseOutputDTOType", bound="BaseOutputDTO", default="BaseOutputDTO")
# BaseStreamOutputDTOType = TypeVar("BaseStreamOutputDTOType", bound="BaseStreamOutputDTO", default="BaseStreamOutputDTO")

# UseCase
class BaseUsecase(Generic[BaseInputDTOType, BaseOutputDTOType], metaclass=ABCMeta):
    """
    ユースケースのベースポリモーフィズム.

    具象クラスではexecuteを実装すること.
    """

    @abstractmethod
    def execute(self, input_dto: BaseInputDTOType) -> BaseOutputDTOType:
        """BaseUsecaseを実行する抽象メソッド."""
        raise NotImplementedError

# # StreamUseCase
# class BaseStreamUsecase(Generic[BaseInputDTOType, BaseStreamOutputDTOType], metaclass=ABCMeta):
#     """
#     ストリームユースケースのベースポリモーフィズム.

#     AsyncGeneratorで型が変わるので分ける
#     具象クラスではexecuteを実装すること.
#     """

#     @abstractmethod
#     async def execute(self, input_dto: BaseInputDTOType) -> AsyncGenerator[BaseStreamOutputDTOType]:
#         """Usecaseを実行する抽象メソッド."""
#         raise NotImplementedError

#         # mypy対策のおまじない
#         # async def メソッドがデフォルトで Coroutine 型として推論されることの対策
#         # https://mypy.readthedocs.io/en/stable/more_types.html#asynchronous-iterators
#         if False:
#             yield 0


#     async def sse_stream(self, input_dto: BaseInputDTOType) -> AsyncGenerator[str]:
#         """
#         UsecaseのexecuteをSSE形式に変換するメソッド.

#         TODO(nonomura): エラーハンドリングを検討する
#         """
#         # 遅延起動する場合
#         # import asyncio
#         # await asyncio.sleep(0.01)
#         async for dto in self.execute(input_dto):
#             yield dto.to_sse() # DTOをSSE形式の文字列に変換して返す



