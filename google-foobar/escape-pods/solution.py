def solution(entrances, exits, path):
    entrance, exit, path = reduce_path(entrances, exits, path)

    flow = 0
    all_paths = get_all_paths(entrance, exit, path)

    if len(all_paths) > 0 and not isinstance(all_paths[0], list):
        all_paths = [all_paths]

    while len(all_paths) > 0:

        for j in range(len(all_paths)):
            mins = []
            cur_path = all_paths[j]
            for i in range(len(cur_path) - 1):
                mins.append(path[cur_path[i]][cur_path[i + 1]])

            min_flow = min(mins)
            for i in range(len(cur_path) - 1):
                path[cur_path[i]][cur_path[i + 1]] -= min_flow

            flow += min_flow

        all_paths = get_all_paths(entrance, exit, path)

    return flow


def get_all_paths(entrance, exit, path):
    rooms = len(path)

    level_graph = [0] * rooms
    level_graph[entrance] = 1

    paths = [[] for i in range(rooms)]

    room_stack = [entrance]

    while len(room_stack) > 0:
        k = room_stack.pop(0)
        l = level_graph[k]
        for i in range(rooms):
            if path[k][i] != 0:
                if level_graph[i] == 0:
                    level_graph[i] = l + 1
                    room_stack.append(i)
                paths[k].append(i)

    all_paths = get_paths(1, [entrance], level_graph, paths, exit)

    return all_paths


def get_paths(cur_l, cur_p, level_graph, paths, exit):
    all_paths = []
    last_el = cur_p[-1]
    if last_el == exit:
        return cur_p
    for i in paths[last_el]:
        if level_graph[i] == cur_l + 1:
            p = get_paths(cur_l + 1, cur_p + [i], level_graph, paths, exit)
            if p:
                all_paths.append(p)
    if len(all_paths) == 1:
        return all_paths[0]
    else:
        return all_paths


def reduce_path(entrances, exits, path):
    rooms = len(path)
    for i in entrances:
        if i == entrances[0]:
            continue
        for j in range(rooms):
            path[entrances[0]][j] += path[entrances[i]][j]
            path[entrances[i]][j] = 0
    removed = entrances[1:]
    entrance = entrances[0]

    for i in exits:
        if i == exits[0]:
            continue
        for j in range(rooms):
            path[j][exits[0]] += path[j][i]
            path[j][i] = 0
    removed += exits[1:]
    exit = exits[0]

    removed.sort(reverse=True)
    for k in removed:
        if k < entrance:
            entrance -= 1
        if k < exit:
            exit -= 1

        path.pop(k)
        rooms -= 1

        for m in range(rooms):
            path[m].pop(k)

    for k in range(rooms):
        path[exit][k] = 0

    for k in range(rooms):
        path[k][entrance] = 0

    return entrance, exit, path
