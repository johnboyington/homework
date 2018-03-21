
def fitness(eol_burnup, max_pppf, max_k_inf):
    A = 8 * (eol_burnup - 46.5)
    B = 4 * (1.30 - max_pppf)
    C = 2 * (1.11 - max_k_inf)
    return A + B + C
