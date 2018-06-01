
class MyClass:
    def method1(self):
        print('myClass method1')

    def method2(self, someString):
        print("myclass method2 " + someString)


class MyOtherClass(MyClass):
    def method1(self):
        MyClass.method1(self)
        print("anotherClass method1")

def main():
    c = MyClass()
    c.method1()
    c.method2("hello python")
    c2 = MyOtherClass()
    c2.method1()
    c2.method2("hello python")

if __name__ == "__main__":
    main()
