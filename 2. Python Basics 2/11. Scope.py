a = 99
def gbs():
    global a
    print(a)
    a = 88
    return a
 
print(gbs())

def fst():
    a = 'parent'
    def snd():
        nonlocal a
        a = 'first child'
        print('first', a)
    snd()    

    def trd():
        global a
        a = 'second child'
        print('second', a)
    trd()
fst()

fst()