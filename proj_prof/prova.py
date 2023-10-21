L = [3,5,1,7]
while len(L) < 8:
    L.append(L[-2] - L[-1])
print(L)