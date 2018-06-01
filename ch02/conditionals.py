


def compare(x, y):
    st = ""
    if(x < y):
        st = "x is less than y"
    elif(x == y):
        st = "x is equal to y"
    else:
        st = "x is greater than y"
    return st

def another_compare(x, y):
    st = "x is less than y" if(x < y) else "x is greater than or the same as y"
    return st

def main():
    x,y = 10, 100
    print(compare(x, y))
    print(another_compare(x, y))
    x = 100
    print(compare(x, y))
    print(another_compare(x, y))
    x = 1000
    print(compare(x, y))
    print(another_compare(x, y))

if __name__ == "__main__":
    main()