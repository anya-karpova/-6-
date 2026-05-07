a = 7
for i in range(a):
    for j in range(a + 1):
        if i == 0 or i == a - 1:
            print("*", end="")
        elif j == i or j == a - i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
