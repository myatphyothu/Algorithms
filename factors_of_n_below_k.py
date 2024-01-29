
def sum_of_factors_of_n_below_k(k, n):
    m = (k - 1) // n
    return n * m * (m + 1) // 2