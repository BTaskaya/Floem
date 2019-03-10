class Dummy:
    def __init__(self, y):
        self.x = y
        print('Flag is greater than 1k')
        for i in range(1323):
            print(i)
        


if __name__ == '__main__':
    d = Dummy(15)
