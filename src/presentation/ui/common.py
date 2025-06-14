def int_gaps(number: int | float) -> str:
    """
    Makes a number look like an integer with gaps.

    For example:
        - 1234 becomes '1 234',
        - 1234567 becomes '1 234 567'.
    """
    return f"{number:_}".replace("_", " ")


def format_percentage(number: int | float) -> str:
    """
    Makes a number look like a percentage.

    For example:
        - 12.34 becomes '+12.34%',
        - 55 becomes '-55%'.
    """
    return f"{number:+}%"
