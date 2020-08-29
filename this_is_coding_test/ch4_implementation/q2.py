def knight(coord):
    row, col = coord[0], coord[1]
    count = 0
    steps = [
        (2, 1), (2, -1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, 2), (-1, -2)
    ]
    for step in steps:
        if -1 < row + step[0] < 8 and -1 < col + step[1] < 8:
            count += 1
    return count
