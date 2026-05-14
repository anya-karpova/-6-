a = []
while True:
    b = int(input("введите пожалуйста число:"))
    if b == 0: 
        break
    a.append(b)

if any(i < 0 for i in a):
    a = [abs(i) for i in a]
print(a)