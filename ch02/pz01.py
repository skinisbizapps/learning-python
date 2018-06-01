
def display_path_to_princess(n, ngrid):
    # print all the moves here
    # find the index position of princess
    # find the index position of the bot
    # x index of princess - x of bot, move that many left else move that many right
    # y of princess - y of bot, move thay many down, else move thany many up
    princess = [(ix, iy) for ix, row in enumerate(ngrid) for iy, i in enumerate(row) if i == "p"]
    bot = [(ix, iy) for ix, row in enumerate(ngrid) for iy, i in enumerate(row) if i == "m"]
    princessy = princess.__getitem__(0)[0]
    princessx = princess.__getitem__(0)[1]
    boty = bot.__getitem__(0)[0]
    botx = bot.__getitem__(0)[1]
    move_right_left = princessx - botx
    moveX = ""
    if move_right_left >= 0:
        move_right_left = abs(move_right_left)
        moveX = "RIGHT"
    else:
        move_right_left = abs(move_right_left)
        moveX = "LEFT"
    move_up_down = princessy - boty
    moveY = ""
    if move_up_down < 0:
        move_up_down = abs(move_up_down)
        moveY = "UP"
    else:
        move_up_down = abs(move_up_down)
        moveY = "DOWN"

    for j in range(0, move_up_down):
        print(moveY)

    for i in range(0, move_right_left):
        print(moveX)


    # print(princess.__getitem__(0)[0], princess.__getitem__(0)[1], type(bot))


if __name__ == "__main__":
    # m = int(input())
    # grid = []
    # for i in range(0, m):
    #    grid.append(input().strip())
    m = 3
    grid = [['-', '-', '-'],
         ['-', 'm', '-'],
         ['p', '-', '-']]
    display_path_to_princess(m, grid)
