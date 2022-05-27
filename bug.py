"""
Bug
"""

from typing import NewType

#: Foo
Foo = NewType("Foo", str)

def foo_to_str(foo: Foo) -> str:
    """
    bar_to_foo
    """
    return foo
