!define flag as 1323
!define name as "floem"

class Dummy:
    def __init__(self, y):
        self.x = y
        !startif <flag> gt 1000
        print('Flag is greater than 1k')
        for i in range(<flag>):
            print(i)
        !endif

if __name__ == '__main__':
    !startif <name> eq "floem"
    d = Dummy(15)
    !endif
    !startif "ksilem" eq <name> 
    print('i dont think so')
    !endif
