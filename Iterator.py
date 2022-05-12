nested_list = [
    ['a', 'b', 'c', [222, '5444', ['222']]],
    ['d', 'e', 'f','h',False, ['22', ['33'], 4]],
    [1, 2, None],
]

# class FlatIterator:
#
#     def __init__(self,nested_list):
#         self.start = -1
#         self.end = len(nested_list)
#         self.nested_list = nested_list
#
#     def __iter__(self):
#         self.start += 1
#         self.index = 0
#         self.new_list = []
#         return self
#
#     def __next__(self):
#         if self.index == len(self.nested_list[self.start]):
#             iter(self)
#         if self.start == self.end:
#             raise StopIteration
#         self.index += 1
#         return self.nested_list[self.start][self.index - 1]

class FlatIterator:

    def __init__(self,nested_list):
        self.start = -1
        self.end = len(nested_list)
        self.nested_list = nested_list
        self.new_list = []

    def __iter__(self):
        self.start += 1
        self.index = 0
        self.len_start = 0
        return self

    def __next__(self):
        if self.index == len(self.nested_list[self.start]):
            iter(self)
        if self.start == self.end:
            raise StopIteration
        self.index += 1
        self.result = self.nested_list[self.start][self.index - 1]
        if isinstance(self.result, list):
            for self.item in self.result:
                self.new_list.append(self.item)
        if isinstance(self.result, (int,str,bool)) or self.result == None:
            self.new_list.append(self.result)
        return self.new_list



for item in FlatIterator(nested_list):
	print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)