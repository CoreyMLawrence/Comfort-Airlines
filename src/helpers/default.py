from typing import Any

def default(value: Any, default: Any) -> Any:
    if not value is None:
        return value
    
    return default