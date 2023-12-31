import requests
from requests.exceptions import RequestException


def generate_random_fact(output_format, language):
    """_summary_

    Args:
        output_format (_type_): _description_
        language (_type_): _description_

    Raises:
        ValueError: _description_
        ValueError: _description_
        RequestException: _description_

    Returns:
        _type_: _description_
    """
    if language not in {"en", "de"}:
        raise ValueError(f"{language} is not supported.")

    if output_format not in {"html", "json", "txt", "md"}:
        raise ValueError(f"{output_format} is not supported.")

    response = requests.get(
        f"https://uselessfacts.jsph.pl/random.{output_format}?language={language}"
    )

    if response.status_code == 200:
        if output_format == "json":
            fact = response.json()
        else:
            fact = response.text
    else:
        raise RequestException(
            f"Something went wrong. Request returned status {response.status_code}."
        )

    return fact
