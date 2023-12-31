from typing import Optional, Iterable

import random
import string


def generate_password(chars: int, punctuation: bool, invalid_chars: Optional[Iterable[str]] = None) -> str:
    """_summary_

    Args:
        chars (int): _description_
        punctuation (bool): _description_
        invalid_chars (Optional[Iterable[str]], optional): _description_. Defaults to None.

    Returns:
        str: _description_
    """
    valid_chars = string.ascii_letters + string.digits

    if punctuation:
        valid_chars += string.punctuation

    for invalid_char in invalid_chars:
        valid_chars = valid_chars.replace(invalid_char, "")

    password_chars = random.choices(valid_chars, k=chars)
    password = "".join(char for char in password_chars)

    return password
