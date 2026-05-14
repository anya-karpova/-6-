a = [1, 2, 3, 4, 5, 6]
chetsum = sum(i for i in a if i % 2 == 0)
nechetsum = sum(i for i in a if i % 2 != 0)
print(chetsum*nechetsum)