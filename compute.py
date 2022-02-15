#!/usr/bin/python3

from __future__ import annotations
import math
from vector import Vector
from math import factorial as facto

def binomial(n: float, k: float) -> float:
    return facto(n)/(facto(k)*facto(n - k))

def bezier(n: float, c: float, t: float) -> float:
    return pow(c/n, t) * pow(1 - (c/n), n-t)

class Point():
    def __init__(self, x_, y_, p_):
        self.x = x_
        self.y = y_
        self.p = p_

    def __str__(self):
        return(f"Point X : {self.x} Y : {self.y} Pollution : {self.p}")
 
class Grid():
    def __init__(self, n_):
        self.grid2D = [[]]
        self.points = []
        self.n = n_

    def push_point(self, point) -> None:
        self.points.append(point)

    def generate(self) -> None:
        self.grid2D = [[0 for _ in range(self.n)] for _ in range(self.n)]
        for p in self.points:
            self.grid2D[p.y][p.x] = p.p

    def get_pollution(self, y, x):
        return self.grid2D[y][x]

    def __str__(self):
        literal = ""
        print("Dumping points...")
        for p in self.points:
            literal += p.__str__() + "\n"
        return literal


def smooth_at(grid: Grid, vec: Vector, n: int) -> float:
    p = 0
    for i in range(n):
        for j in range(n):
            p += binomial(n-1, i) * binomial(n-1, j) * bezier(n-1, vec.x, i) * \
                 bezier(n-1, vec.y, j) * grid.get_pollution(i, j)
    return p
