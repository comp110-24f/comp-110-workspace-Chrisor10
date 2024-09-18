def loop(stop: int) -> None:
    condition: bool = True
    num_loops: int = 0
    if condition:
        print(num_loops)
        num_loops = num_loops + 1
        if num_loops >= stop:
            condition = False


loop(stop=2)
