
def main():
    print('welcome to loops')

    x = 0
    # define a while loop
    while x < 5:
        print(x)
        x = x + 1

    # define a for loop
    for x in range(5, 10):
        print(x)

    # use a for loop over a collection
    days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    for day in days:
        print(day)
    # use the break and continue statements
    for x in range(5, 10):
        # continue skip printing the x but moves on the next value
        if x % 2 == 0:
            continue

        # break stops any further processing and exits out of the loop
        if x == 9:
            break

        print(x)

    # using the enumerate() function to get index
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    for i, month in enumerate(months):
        print(month, i + 1)

if __name__ == '__main__':
    main()
