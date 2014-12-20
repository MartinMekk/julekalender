__author__ = 'martinsolheim'


def test_valid_position(pos):
    x = abs(pos[0])
    y = abs(pos[1])
    sum_x = sum(map(int, str(x)))
    sum_y = sum(map(int, str(y)))
    return sum_x + sum_y <= 19


tiles_list = [(0, 0)]
count = 1

for tile in tiles_list:
    x = tile[0]
    y = tile[1]
    if test_valid_position([x + 1, y]):
        if (x+1, y) not in tiles_list:
            tiles_list.append((x + 1, y))
            if y == 0 or x + 1 == 0:
                count += 2
            else:
                count += 4
    if test_valid_position([x, y + 1]):
        if (x, y+1) not in tiles_list:
            tiles_list.append((x, y + 1))
            if y + 1 == 0 or x == 0:
                count += 2
            else:
                count += 4

print(count)