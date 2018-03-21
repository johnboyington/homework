import numpy as np
from numpy.random import randint

material_library = []

u235_percentages = np.arange(2.0, 5.0, 0.1)
gd_percentages = np.array([0] + list(range(2, 11, 1)))


for u in u235_percentages:
    for g in gd_percentages:
        material_library.append((u, g))


def rand_material():
    return material_library[randint(0, len(material_library))]
