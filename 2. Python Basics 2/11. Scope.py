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

# Scope - what variables do I have access to?
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)
outer()

#1 - start with local
#2 - Parent local?
#3 - global
#4 - built in python functions