print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 300
if b > a :
    print("b is greater than a")
else :
    print ("b is not greater than a")

print (bool("hello"))
print (bool(15))

class myclass() :
    def _len_(self):
        return 0
myboj = myclass()
print(bool(myboj))

def myFunction() :
    return True
if myFunction() :
    print("yes")
else:
    print("NO!")
    