def int_gaps(number: int | float) -> str:
    return f"{number:_}".replace("_", " ")


def format_percentage(number: int | float) -> str:
    return f"{number:+}%"
