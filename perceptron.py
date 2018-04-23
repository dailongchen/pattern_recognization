class Vector:
    def __init__(self, vector_data):
        self.data = vector_data

    def __mul__(self, other):
        if isinstance(other, Vector):
            result = 0
            for i in range(len(self.data)):
                result += self.data[i] * other.data[i]

            return result
        else:
            return Vector(list(x * other for x in self.data))

    def __iadd__(self, other):
        if isinstance(other, Vector):
            for i in range(len(self.data)):
                self.data[i] += other.data[i]
        else:
            for i in range(len(self.data)):
                self.data[i] += other

        return self

    def __str__(self):
        return str(self.data)


class Data:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def calc_y(data, w, b):
    return w * data.x + b


def training(data_list, w, b, learning_rate):
    changed = False
    for data in data_list:
        if data.y * calc_y(data, w, b) <= 0:
            w += data.x * (learning_rate * data.y)
            b += learning_rate * data.y
            changed = True

    return changed, b


if __name__ == '__main__':
    data_list = [Data(Vector([-2, -2]), -1), Data(Vector([-1, -1]), -1), Data(Vector([0, 1]), -1), Data(Vector([4, 3]), -1),
                 Data(Vector([5, 5]), 1), Data(Vector([10, 9]), 1), Data(Vector([13, 12]), 1)]
    w = Vector([0, 0])
    b = 0
    learning_rate = 0.1

    loop_count = 0
    for i in range(1000):
        loop_count += 1
        changed, b = training(data_list, w, b, learning_rate)
        if not changed:
            break

    for data in data_list:
        print(data.x, data.y, '=>', data.x * w + b)

    print('\nloop:', loop_count, '\nw:', w, '\nb:', b)
