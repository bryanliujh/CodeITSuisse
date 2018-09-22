import logging

from flask import request, jsonify
from codeitsuisse import app;
from codeitsuisse.routes.solver import Solver
import numpy as np

logger = logging.getLogger(__name__)

@app.route('/sorting-game', methods=['POST'])
def sorting_game():
    myarr = []
    data = request.get_json()
    for item_arr in data["puzzle"]:
        for item in item_arr:
            myarr.append(item)
            '''
            if item == 0:
                index_no = item_arr.index(0)
                logging.info(index_no)
            '''
    logging.info(myarr)
    text = np.array(myarr)
    init_state = text.reshape((3,3))

    goal_state = np.array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 0]])


    heuristic = "manhattan"
    max_iter = 10000

    #logging.info(A_star(init_state, goal_state, max_iter, heuristic))
    my_array = np.array(A_star(init_state, goal_state, max_iter, heuristic), dtype=int).tolist()
    new_dic = {"result": my_array}
    logging.info(new_dic)

    ''''
    logging.info(matrix_arr)
    i, j = np.where(matrix_arr == 0)
    logging.info(i)
    logging.info(j)
    '''
    return jsonify(new_dic)


def A_star(init_state, goal_state, max_iter, heuristic):
    solver = Solver(init_state, goal_state, heuristic, max_iter)
    path = solver.solve_a_star()
    path_arr = []

    if len(path) == 0:
        exit(1)

    init_idx = init_state.flatten().tolist().index(0)
    init_i, init_j = init_idx // goal_state.shape[0], init_idx % goal_state.shape[0]


    for node in reversed(path):
        cur_idx = node.get_state().index(0)
        cur_i, cur_j = cur_idx // goal_state.shape[0], cur_idx % goal_state.shape[0]

        new_i, new_j = cur_i - init_i, cur_j - init_j
        if new_j == 0 and new_i == -1:
            print('Moved UP    from ' + str((init_i, init_j)) + ' --> ' + str((cur_i, cur_j)))
        elif new_j == 0 and new_i == 1:
            print('Moved DOWN  from ' + str((init_i, init_j)) + ' --> ' + str((cur_i, cur_j)))
        elif new_i == 0 and new_j == 1:
            print('Moved RIGHT from ' + str((init_i, init_j)) + ' --> ' + str((cur_i, cur_j)))
        else:
            print('Moved LEFT  from ' + str((init_i, init_j)) + ' --> ' + str((cur_i, cur_j)))


        # 6
        new_pos = init_state[cur_i, cur_j]
        # 0
        old_pos = init_state[init_i, init_j]
        path_arr.append(init_state[cur_i, cur_j])
        init_state[init_i, init_j] = new_pos
        init_state[cur_i, cur_j] = old_pos





        init_i, init_j = cur_i, cur_j

        '''
        for i in range(goal_state.shape[0]):
            print(np.array(node.get_state()).reshape(goal_state.shape[0], goal_state.shape[0])[i, :])
        print()
        '''
    return path_arr



