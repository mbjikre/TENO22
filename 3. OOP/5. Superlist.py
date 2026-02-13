class Sp(list):
    def __len__(self):
        return 1000
    
sp = Sp()
print(len(sp))
sp.append(5)
print(sp[0])