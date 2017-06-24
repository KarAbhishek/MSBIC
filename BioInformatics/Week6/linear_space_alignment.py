from utils import middle_node
from utils import middle_edge
from utils import pathleft, pathtop

def linear_space_alignment(v, w, top, bottom, left, right, path_top, path_left):
    if left == right:
        print(path_top(top, bottom, left, right))#output path formed by bottom − top vertical edges
    if top == bottom:
        print(path_left(top, bottom, left, right))#output path formed by right − left horizontal edges
    middle = len((left + right + 1)/2)
    midNode = middle_node(top, bottom, left, right)
    midEdge = middle_edge(top, bottom, left, right)
    linear_space_alignment(v, w, top, midNode, left, middle, path_top, path_left)
    print(midEdge)
    if midEdge == "R" or midEdge == "C":
        middle += 1
    if midEdge == "D" or midEdge =="C":
        midNode += 1
    linear_space_alignment(v, w, midNode, bottom, middle, right, path_top, path_left)