"""Implementing utility functions"""

__author__ = "730654279"


def invert(x: dict[str, str]) -> dict[str, str]:
    """inverts the keys and values of the dict"""
    invert: dict[str, str] = {}
    for key in x:
        value = x[key]
        if value in invert:
            raise KeyError(f"A duplicate value found here: {value} for {key}")
        invert[value] = key
    return invert


def favorite_color(x: dict[str, str]) -> str:
    """the color that appears most frequently"""
    color_num: dict[str, int] = {}
    first: dict[str, str] = {}
    for name in x:
        color = x[name]
        if color in color_num:
            color_num[color] += 1
        else:
            color_num[color] = 1
            first[color] = name
    popular: str = ""  # checking if there's a tie
    max_num: int = 0
    for color in color_num:
        num = color_num[color]
        if num > max_num or (num == max_num and first[color] < first[popular]):
            popular = color
            max_num = num
    return popular


def count(x: list[str]) -> dict[str, int]:
    """count the number of times a value has appeared"""
    result: dict[str, int] = {}
    for item in x:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def alphabetizer(x: list[str]) -> dict[str, list[str]]:
    """alphabetize the list by the first letter of the word"""
    result: dict[str, list[str]] = {}
    for word in x:
        first_letter = word[
            0
        ].lower()  # getting the first character to always be lower cased
        if first_letter not in result:
            result[first_letter] = []
        result[first_letter].append(word)
    return result


def update_attendance(x: dict[str, list[str]], day: str, student: str) -> None:
    """Update attendance with new information"""
    if day in x:
        if student not in x[day]:  # check if the student isn't already on the list
            x[day].append(student)
    else:
        x[day] = [student]
