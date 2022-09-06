class FlatIterator:
    def __init__(self, nested_list):
        self.nested_list = nested_list

    def __iter__(self):
        self.counter = 0
        self.inner_counter = 0
        return self

    def __next__(self):
        if self.counter < len(self.nested_list):
            if self.inner_counter < len(self.nested_list[self.counter]):
                y = self.nested_list[self.counter][self.inner_counter]
                self.inner_counter += 1
                return y
            else:
                self.inner_counter = 0
                self.counter += 1
                if self.counter == len(self.nested_list):
                    raise StopIteration
                y = self.nested_list[self.counter][self.inner_counter]
                self.inner_counter += 1
                return y


def test_case():
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]
    for item in FlatIterator(nested_list):
        print(item)


if __name__ == '__main__':
    test_case()
