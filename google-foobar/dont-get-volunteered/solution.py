def solution(src, dest):
    maxPosition = 63
    minPosition = 0
    #dict of all possible tiles with distance from source to destination
    positions = dict(zip(range(minPosition, maxPosition + 1), [-1] * (maxPosition - minPosition + 1)))
    #possible shifts with columns difference
    possibleShifts = {"-17": -1, "-15": 1, "-10": -2, "-6": 2, "6": -2, "10": 2, "15": -1, "17": 1}
    #queue of moves to check
    moves = []

    positions[dest] = 0
    moves.append(dest)

    while len(moves) > 0:
        elem = moves.pop(0)
        dist = positions[elem]
        if elem == src:
            return dist

        for shift in possibleShifts:
            new_elem = elem + int(shift)
            if new_elem in positions and positions[new_elem] == -1 and elem % 8 + possibleShifts[shift] >= 0 and elem % 8 + possibleShifts[shift] <= 7:
                positions[new_elem] = dist + 1
                moves.append(new_elem)
