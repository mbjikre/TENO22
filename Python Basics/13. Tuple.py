tup = (1,2,3,4,5)
print(tup.index(5))

ttup = (1,2,3,4,5)
ntup = ttup[::]
print(ntup)

stup = (range(1,100))
print(list(stup[2:50:3]))

ftp = (1,2,3,4,5,2,2)
print(len(ftp))

fset = {1,2,3,4,5,5}
fset.add(100)
fset.add(2)
print(fset)

sset = set(ftp)
print(sset)

tset = {1,2,3,4,5,5,5}
fset = tset.copy()
tset.clear()
print(fset)
print(tset)

ftset = {1,2,3,4,5,6,7}
siset = {3,4,5,6,7,8,9}
