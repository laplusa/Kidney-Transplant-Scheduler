from blossom import find_maximum_matching
from demo import giveinput, show_demo
import sys

def run():
    file = open("b.input","r")
    sys.stdin = file
    vertices = {}
    num_node,num_edge = input().split()
    num_node = int(num_node)
    num_edge = int(num_edge)
    for _ in range(num_edge):
        x, y, z = input().split()
        x = int(x)
        y = int(y)
        vertices[x, y] = 0
        if x > num_node or y > num_node:
            print("wrong input try again")
            exit(0)
    show_demo(vertices, num_node, num_edge)
run()
