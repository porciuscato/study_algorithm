



def go():
    c = 30
    def gogo():
        global c
        c = 20
        print(c)
    gogo()
    print(c)

a = 10
b = 20
c = 40
go()
print(c)