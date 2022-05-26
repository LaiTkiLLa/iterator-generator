nested_list = [
    ['a', 'b', 'c', ['11', 22, 33]],
    ['d', 'e', 'f','h',False],
    [512],
    [1, 2, None],
    [2222, '22424'],
    [224142132, '1234']
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

    def __init__(self, some_list):
        self.main_list = some_list


    def __iter__(self):
        self.main_list_cursor = 0  # курсор основного списка
        self.nested_list_cursor = 0  # курсор списка вложенного в основной список
        return self

    def __next__(self):

        if self.nested_list_cursor < len(self.main_list[self.main_list_cursor][self.nested_list_cursor]):
            self.nested_list_cursor += 1
            for self.item in self.main_list[self.main_list_cursor][self.nested_list_cursor - 1]:
               return self.item

        if self.nested_list_cursor == len(self.main_list[self.main_list_cursor][self.nested_list_cursor]):
            self.main_list_cursor += 1
            self.nested_list_cursor == 0
            for self.item in self.main_list[self.main_list_cursor][self.nested_list_cursor]:
               return self.item

        if self.main_list_cursor == len(self.main_list) and self.nested_list_cursor == len(self.main_list[self.main_list_cursor]):
            raise StopIteration

        return self.main_list[self.main_list_cursor][self.nested_list_cursor]




flat_list = []
for item in FlatIterator(nested_list):
   flat_list.append(item)
   print(flat_list)

# flat_list = [item for item in FlatIterator(nested_list)]
# print(flat_list)