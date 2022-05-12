nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False, [111, '222', False]],
	[1, 2, None],
]

# def flat_generator(nested_list):
# 	for item in nested_list:
# 		if isinstance(item, list):
# 			for new_item in item:
# 				if isinstance(new_item, (str,bool,int)) or new_item == None:
# 					yield new_item



def flat_generator(nested_list):
	for item in nested_list:
		if isinstance(item, list):
			for new_item in flat_generator(item):
				yield new_item
		else:
			yield item

for item in flat_generator(nested_list):
	print(item)

flat_list = [item for item in flat_generator(nested_list)]
print(flat_list)