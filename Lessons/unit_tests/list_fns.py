""""""


def get_first(input: list[str]) -> str:
    """return first elem"""
    return input[0]


def remove_first(input: list[str]) -> None:
    """removing first elem"""
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    """remove AND return first elem"""
    first_elem: str = input[0]
    # this saves the first elem in memory and does't disappear so that we can call it
    input.pop(0)  # remove elem
    return first_elem
