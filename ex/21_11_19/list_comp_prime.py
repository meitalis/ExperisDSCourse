
l = [x for x in range(100) if all(x % y !=0 for y in range(2,x))]
print(l)
