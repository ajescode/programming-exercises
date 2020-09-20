import itertools


def solution(times, times_limit):
    spots = len(times)
    # Floyd Warshall algorithm

    graph = reduceGraph(times)

    for i in range(spots):
        if times[i][i] < 0:
            return [x for x in range(spots - 2)]

    paths = getPaths(spots - 2)

    best_l = 0
    for i in paths[1:]:
        sum = 0
        for j in range(len(i) - 1):
            sum += graph[i[j]][i[j + 1]]
        if sum <= times_limit and len(i) > best_l:
            best_path = i
            best_l = len(i)

    best_path = sorted(map(lambda x: x - 1, best_path[1:-1]))

    return best_path


def getPaths(bunnies):
    entrance = 0
    exit = bunnies + 1
    paths = []
    for i in reversed(range(bunnies + 1)):
        for path in itertools.permutations(range(1, bunnies + 1), i):
            path = [entrance] + list(path) + [exit]
            paths.append(path)

    return paths


def reduceGraph(times):
    spots = len(times)

    for i in range(spots):
        for j in range(spots):
            for k in range(spots):
                if times[i][j] > times[i][k] + times[k][j]:
                    times[i][j] = times[i][k] + times[k][j]

    return times
