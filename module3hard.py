def calculate_structure_sum(struct):
  s = 0
  for item in struct:
    if isinstance(item, list) or isinstance(item, tuple) or isinstance(item, set):
      s += calculate_structure_sum(item)
    elif isinstance(item, dict):
      item = list(item.items())
      s += calculate_structure_sum(item)
    elif isinstance(item, str):
      s += len(item)
    else:
      s += item
  return s


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)