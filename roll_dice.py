import dice

repeat = True

dice1 = dice.dice(6)

while repeat:
    print("You rolled " + str(dice1.roll()) + ", continue?")
    repeat = ("y" or "yes") in input().lower()
