__author__ = 'martinsolheim'

import copy


def state_machine(from_state):
    if from_state == 1:
        return 6, 8
    elif from_state == 2:
        return 7, 9
    elif from_state == 3:
        return 4, 8
    elif from_state == 4:
        return 0, 3, 9
    elif from_state == 6:
        return 0, 1, 7
    elif from_state == 7:
        return 2, 6
    elif from_state == 8:
        return 1, 3
    elif from_state == 9:
        return 2, 4
    elif from_state == 0:
        return 4, 6
    else:
        return -1


node_list = [[1]]
while len(node_list[0]) < 10:
    list_length = len(node_list)
    for i in range(0, list_length):
        sub_list = node_list[i]
        next_move = list(state_machine(sub_list[-1]))
        new_node = copy.copy(sub_list)
        new_node.append(next_move[1])
        node_list.append(new_node)
        if len(next_move) > 2:
            new_node = copy.copy(sub_list)
            new_node.append(next_move[2])
            node_list.append(new_node)
        sub_list.append(next_move[0])


print(len(node_list))