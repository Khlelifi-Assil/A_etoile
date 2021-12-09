import numpy as np

import numpy as np

class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def return_chemin(node_courant, grille):
    chemin = []
    no_rows, no_columns = np.shape(grille)

    resultat = [[-1 for i in range(no_columns)] for j in range(no_rows)]
    courant = node_courant
    while courant is not None:
        chemin.append(courant.position)
        courant = courant.parent

    chemin = chemin[::-1]
    valeur_debut = 0

    for i in range(len(chemin)):
        resultat[chemin[i][0]][chemin[i][1]] = valeur_debut
        valeur_debut += 1
    return resultat


def chercher(grille, cost, debut, fin):

    debut_node = Node(None, tuple(debut))
    debut_node.g = debut_node.h = debut_node.f = 0
    end_node = Node(None, tuple(fin))
    end_node.g = end_node.h = end_node.f = 0

    yet_to_visit_list = []
    visited_list = []
    yet_to_visit_list.append(debut_node)
    outer_iterations = 0
    max_iterations = (len(grille) // 2)**10
    move = [[-1, 0], [0, -1], [1, 0], [0, 1]]

    no_rows, no_columns = np.shape(grille)

    while len(yet_to_visit_list) > 0:
        outer_iterations += 1
        node_courant = yet_to_visit_list[0]
        courant_index = 0
        for index, item in enumerate(yet_to_visit_list):
            if item.f < node_courant.f:
                node_courant = item
                courant_index = index
        if outer_iterations > max_iterations:
            print("Plusieurs Iteration, operation annullée")
            return return_chemin(node_courant, grille)

        yet_to_visit_list.pop(courant_index)
        visited_list.append(node_courant)

        if node_courant == end_node:
            return return_chemin(node_courant, grille)

        children = []

        for new_position in move:

            node_position = (node_courant.position[0] + new_position[0],
                             node_courant.position[1] + new_position[1])

            if (node_position[0] > (no_rows - 1) or node_position[0] < 0
                    or node_position[1] > (no_columns - 1)
                    or node_position[1] < 0):
                continue

            if grille[node_position[0]][node_position[1]] != 0:
                continue

            new_node = Node(node_courant, node_position)

            children.append(new_node)

        for child in children:

            if len([
                    visited_child
                    for visited_child in visited_list if visited_child == child
            ]) > 0:
                continue

            child.g = node_courant.g + cost
            child.h = (((child.position[0] - end_node.position[0])**2) +
                       ((child.position[1] - end_node.position[1])**2))

            child.f = child.g + child.h
            if len(
                [i for i in yet_to_visit_list if child == i and child.g > i.g
                 ]) > 0:
                continue
            yet_to_visit_list.append(child)

def heuristique(grille, cost, debut, fin):
    
    chemin = chercher(grille, cost, debut, fin)
   
    return chemin
 