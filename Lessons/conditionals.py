""""Practicing conditionals"""


def less_than_10(num: int) -> None:
    """Tell us if num < 10"""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:  # check if this is true
        print("Small number")  # "then" block
    else:
        print("Big number")
    print("This is the end of the function")


less_than_10(num=7)


def wake_up(alarm: bool) -> str:
    """Return message based on if alarm is going off"""
    if alarm is True:
        return "Wake up!"
    else:
        return "Keep sleeping"


def check_first_letter(word: str, letter: str) -> str:
    """Checks if letter matches the first letter of word"""
    if word[0] == letter:
        return "Match"
    else:
        return "No match"


# print(check_first_letter(word="happy", letter="h"))
# print(check_first_letter(word="happy", letter="s"))

"""Practice with elif function"""


def get_weather_report() -> str:
    """Asking the weather"""
    weather: str = input("What is the weather?")
    if (weather == "rainy") or (weather == "cold"):
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather
