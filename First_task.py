class FlatIterator:
	def __init__(self, data):
		self.data = data

	def __iter__(self):
		self.count1 = 0
		self.count2 = -1
		return self

	def __next__(self):
		self.count2 += 1
		if self.count2 == len(self.data[self.count1]):
			self.count1 += 1
			self.count2 = 0
		if self.count1 == len(self.data):
			raise StopIteration
		return self.data[self.count1][self.count2]


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None]
]

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)
