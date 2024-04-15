from __future__ import annotations
from typing import Iterable, Any

def first(predicate, iterable: Iterable) -> Any:
    for item in iterable:
        if predicate(item):
            return item
        
    return None

def first_or_error(predicate, iterable: Iterable) -> Any:
    for item in iterable:
        if predicate(item):
            return item
        
    raise RuntimeError()