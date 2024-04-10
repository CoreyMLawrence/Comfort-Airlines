from __future__ import annotations
from typing import Union, Iterable

def first[T](predicate, iterable: Iterable[T]) -> Union[T,None]:
    for item in iterable:
        if predicate(item):
            return item
        
    return None
    