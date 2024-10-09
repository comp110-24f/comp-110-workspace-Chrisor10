""""For In Loops Practice"""

pets: list[str] = ["Louie", "Bo", "Bear"]
for elem in pets:
    print(f"Good boy, {elem}!")

# using range() in a "for...in loop
names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range(0, len(names)):
    print(f"{idx}: {names[idx]}")
