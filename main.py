import u2
from reporting import *

problem = u2.A((1, 1, 1, 1, 1, 1, 1, 1, 0, 3600))
# print("exp = {}".format(problem.exp))
solution = breadth_first_graph_search(problem)
# print("eye = {}".format(problem.eye))
path = path_actions(solution)
n_pauses = path.count("pause")
n_moves = len(path) - n_pauses
path = list(filter(lambda x: x != "pause", path))
new_path = []
if n_pauses % n_moves != 0:
    mod = n_pauses % n_moves
else:
    mod = 0
for i in range(n_moves+1):
    new_path.extend(["pause"] * ((n_pauses // n_moves) + mod))
    if i != (n_moves):
        new_path.append(path.pop())
    mod = 0
print(new_path)
cost = solution.path_cost
print('cost = {}'.format(cost))
