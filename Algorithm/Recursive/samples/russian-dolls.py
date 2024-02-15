def openRussianDoll(doll):
    if doll == 1:
        print("Smallest doll opened")
    else:
        openRussianDoll(doll - 1)
        print(f"Doll {doll} opened")

print(openRussianDoll(5))
