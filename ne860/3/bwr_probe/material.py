import numpy as np
from numpy.random import randint
from math import isclose

material_library = []

u235_percentages = np.arange(2.0, 5.0, 0.1)
gd_percentages = np.array([0] + list(range(2, 11, 1)))


for u in u235_percentages:
    for g in gd_percentages:
        material_library.append((u, g))


def rand_material():
    return material_library[randint(0, len(material_library))]


def mat_id(u235, gd):
    for i, mat in enumerate(material_library):
        if mat[1] == gd:
            if isclose(mat[0], u235):
                return i
