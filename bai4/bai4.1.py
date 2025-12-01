# Võ Tá Cường , MSV: 245752021610100
# Định nghĩa module toán học mymath

def square(n):
    return n * n

def cube(n):
    return n * n * n

def average(values):
    nvals = len(values)
    total = 0.0
    for v in values:
        total += v
    return float(total) / nvals
