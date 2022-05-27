"""
Bar
"""

from typing import Annotated
from typing import NewType
from . import foo as _foo

#: Bar
Bar = NewType("Bar", "Annotated[str, 'bar']")

def foo_to_bar(foo: "_foo.Foo") -> Bar:
    """
    foo_to_bar
    """
    return str(foo)  # type: ignore
