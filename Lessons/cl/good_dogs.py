"""Recursion practice over a list"""


def all_good(scores: list[dict[str, str]], thresh: int, idx: int) -> bool:
    num_dogs: int = len(scores)
    if num_dogs <= idx:
        raise IndexError("idx is too high")
    elif int(scores[idx]["score"]) < thresh:  #
        return False
    else:
        if num_dogs == idx + 1:
            return True
        else:
            # make we are making foward progress in the recursive case
            return all_good(scores, thresh, idx + 1)


pack: list[dict[str, str]] = [
    {"name": "Nelli", "score": "10"},
    {"name": "Ada", "score": "9"},
    {"name": "Pip", "score": "7"},
]

print(all_good(scores=pack, thresh=8, idx=0))
