from slowpy.ndarray import Array


def ones(shape):
    a = Array(shape)
    return a.fill(1)


def zeros(shape):
    a = Array(shape)
    return a.fill(0)


def array(a):
    rows = len(a)
    cols = len(a[0])

    arr = Array((rows, cols))
    arr.data = [v for v in [row for row in a]]
    return arr