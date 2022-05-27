"""
Foo
"""

from typing import Annotated
from typing import NewType
from . import bar as _bar

#: Foo
Foo = NewType("Foo", "Annotated[str, 'foo']")

def bar_to_foo(bar: "_bar.Bar") -> Foo:
    """
    bar_to_foo
    """
    return str(bar)  # type: ignore
