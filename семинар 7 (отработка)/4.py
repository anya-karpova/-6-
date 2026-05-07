import random
a = random.randint(0, 100)
for i in range (1, 11):
    user = int(input("введите пожалуйста число:"))

    if user == a:
        print("поздравляю, вы угадали!")
        break
    elif user > a:
        print("ваше число меньше чем загаданное, попробуйте еще")
    else:
         print("ваше число больше чем загаданное, попробуйте еще")

else:
    print("простите, но попытки кончились")
    print(a)