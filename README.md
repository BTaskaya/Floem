# Floem
Segmented Python Preprocessor
## Precommands
Precommands starts with `!` symbol and continues with directive.
### Define Directive
Defines a static variable and when preprocessing fills all parts with that variable. It can take any value. Example;
```
!define flag as 1323
!define name as "floem"
```

### Control Flow Directive
Compares 2 static at preprocessing time and if comperation successfully occurs it allows the code inside the `!startif` & `!endif` directives to run. If not the code just be deleted.
```py
class Dummy:
    def __init__(self, y):
        self.x = y
        !startif <flag> gt 1000
        print('Flag is greater than 1k')
        for i in range(<flag>):
            print(i)
        !endif
```
### Example
```py
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
```
and after the preprocessing
```
class Dummy:
    def __init__(self, y):
        self.x = y
        print('Flag is greater than 1k')
        for i in range(1323):
            print(i)

if __name__ == '__main__':
    d = Dummy(15)
```
