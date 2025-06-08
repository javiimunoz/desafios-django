def values_greater_than_second(lst):
  if len(lst) < 2:
    return False
  second_value = lst[1]
  new_list = [value for value in lst if value > second_value]
  print(len(new_list))
  return new_list

# Ejemplos de uso:
print(values_greater_than_second([5, 2, 3, 2, 1, 4]))  # Debería imprimir 3 y devolver [5, 3, 4]
print(values_greater_than_second([3]))  # Debería devolver False26