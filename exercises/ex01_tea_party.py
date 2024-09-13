"""Tea Party Exercise"""

__author__: str = "730654279"


def main_planner(guest: int) -> None:
    """Main details of tea party"""
    print(("A Cozy Tea Party for ") + str(guest) + (" People!"))
    print("Tea Bags: " + str(tea_bags(guest)))
    print(("Treats: ") + str(treats(guest)))
    print(("Cost: ") + "$" + str(cost(tea_bags(guest), treats(guest))))


def tea_bags(people: int) -> int:
    """Return the number of tea bags per person"""
    return 2 * people


def treats(people: int) -> int:
    """Return the number of treats per person"""
    return int(tea_bags(people=people) * 1.5)


# remember to return with the right type as in signature


def cost(tea_count: int, treat_count: int) -> float:
    """Cost of tea bags and treats"""
    return (tea_count * 0.50) + (treat_count * 0.75)


# tea_count/treat_count is the number of tea bags and treats needed

if __name__ == "__main__":
    main_planner(guest=int(input("How many guest are attending your tea party?")))
