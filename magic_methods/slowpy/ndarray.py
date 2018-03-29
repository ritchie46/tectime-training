from functools import reduce

# limited to 2d arrays


class Array:
    def __init__(self, shape):
        assert(isinstance(shape, tuple))
        self.shape = shape
        self.data = None
        self.index = 0

    @property
    def _shape(self):
        if len(self.shape) == 2:
            return self.shape
        else:
            return 1, self.shape[0]

    def fill(self, value):
        a = Array(self.shape)
        a.data = [[value for col in range(self._shape[-1])] for row in range(self._shape[0])]
        return a

    def flatten(self):
        a = Array(self.shape)
        a.data = [[v for row in self.data for v in row]]
        return a

    def apply_function_elementwise(self, other, function):
        a = Array(self.shape)
        a.data = []
        for row_1, row_2 in zip(self.data, other.data):
            new_row = []
            for v1, v2 in zip(row_1, row_2):
                new_row.append(function(v1, v2))
            a.data.append(new_row)
        return a

    def __str__(self):
        return 'array:\n' + '\n'.join([''.join(['{:4}'.format(a) for a in row]) for row in self.data])

    def __len__(self):
        return reduce(lambda a, b: a * b, self.shape)

    def __add__(self, other):
        # array + array
        if isinstance(other, Array):
            return self.apply_function_elementwise(other, lambda x, y: x + y)
        # array + int
        if isinstance(other, (int, float)):
            a = Array(self.shape)
            a.data = []
            a.data = [list(map(lambda x: x + other, v)) for v in [row for row in self.data]]
            return a

    def __radd__(self, other):
        assert isinstance(other, (int, float))
        return self.__add__(other)

    def __mul__(self, other):
        # array * array
        if isinstance(other, Array):
            return self.apply_function_elementwise(other, lambda x, y: x * y)
        # array * int
        if isinstance(other, (int, float)):
            a = Array(self.shape)
            a.data = []
            a.data = [list(map(lambda x: x + other, v)) for v in [row for row in self.data]]

    def __rmul__(self, other):
        assert isinstance(other, (int, float))
        return self.__mul__(other)

    def __sub__(self, other):
        # array - array
        if isinstance(other, Array):
            return self.apply_function_elementwise(other, lambda x, y: x - y)

        # array - int
        if isinstance(other, (int, float)):
            a = Array(self.shape)
            a.data = []
            a.data = [list(map(lambda x: x - other, v)) for v in [row for row in self.data]]
            return a

    def __rsub__(self, other):
        a = Array(self.shape)
        # int - array
        if isinstance(other, (int, float)):
            a.data = [list(map(lambda x: other - x, v)) for v in [row for row in self.data]]
        return a

    def __eq__(self, other):
        if isinstance(other, Array):
            if self.shape == other.shape:
                return all([v1 == v2 for v1, v2 in zip(self.flatten().data, other.flatten().data)])
            else:
                return False

    def __getitem__(self, item):
        # slicing works
        if isinstance(item, int):
            return self.data[item]
        if isinstance(item, tuple):
            return self.data[item[0]][item[1]]

    def __iter__(self):
        for x in self.flatten().data[0]:
            yield x





