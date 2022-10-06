while True:
    w, h = map(int, input().split())
    if w + h == 0:
        break
    count = 0
    maps = [list(map(int, input().split())) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                count += 1
                maps[i][j] = 0
                spots = [[i, j]]
                while spots != []:
                    temp = []
                    for spot in spots:
                        y, x = spot[0], spot[1]
                        # 상
                        if y-1 >= 0:
                            if maps[y-1][x] == 1:
                                maps[y-1][x] = 0
                                temp += [[y-1, x]]
                        # 하
                        if y+1 <= h-1:
                            if maps[y+1][x] == 1:
                                maps[y+1][x] = 0
                                temp += [[y+1, x]]
                        # 좌
                        if x-1 >= 0:
                            if maps[y][x-1] == 1:
                                maps[y][x-1] = 0
                                temp += [[y, x-1]]
                        # 우
                        if x+1 <= w-1:
                            if maps[y][x+1] == 1:
                                maps[y][x+1] = 0
                                temp += [[y, x+1]]
                        # 좌상
                        if y-1 >= 0 and x-1 >= 0:
                            if maps[y-1][x-1] == 1:
                                maps[y-1][x-1] = 0
                                temp += [[y-1, x-1]]
                        # 우상
                        if y-1 >= 0 and x+1 <= w-1:
                            if maps[y-1][x+1] == 1:
                                maps[y-1][x+1] = 0
                                temp += [[y-1, x+1]]
                        # 우하
                        if x+1 <= w-1 and y+1 <= h-1:
                            if maps[y+1][x+1] == 1:
                                maps[y+1][x+1] = 0
                                temp += [[y+1, x+1]]
                        # 좌하
                        if x-1 >= 0 and y+1 <= h-1:
                            if maps[y+1][x-1] == 1:
                                maps[y+1][x-1] = 0
                                temp += [[y+1, x-1]]
                    spots = temp
    print('count:',count)