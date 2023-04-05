import re


def extract_pep_data(pep_heading: str) -> tuple[str]:
    """Извлекает из заголовка PEP его номер и название."""
    pattern = r'^PEP (?P<number>\d+) – (?P<name>.*)'
    heading_match = re.search(pattern, pep_heading)
    number, name = heading_match.groups()
    return number, name
