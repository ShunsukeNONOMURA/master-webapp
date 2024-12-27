from collections.abc import Callable
from typing import Any

from pydantic.alias_generators import to_camel, to_snake


def recursive_to_convert(d: dict[str,Any], convert: Callable[[str],str]) -> dict[str,Any]:
    """
    再帰的にケース変換を行う.

    ケースが混ざると後勝ちになる
    """
    new_d = {}
    for k, v in d.items():
        new_d[convert(k)] = recursive_to_convert(v,convert) if isinstance(v,dict) else v
    return new_d

def recursive_to_camel(d: dict[str,Any]) -> dict[str,Any]:
    return recursive_to_convert(d, to_camel)

def recursive_to_snake(d: dict[str,Any]) -> dict[str,Any]:
    return recursive_to_convert(d, to_snake)
