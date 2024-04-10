from __future__ import annotations
from typing import Union, Iterable, Any

def first(predicate, iterable: Iterable) -> Any:
    for item in iterable:
        if predicate(item):
            return item
        
    return None
    