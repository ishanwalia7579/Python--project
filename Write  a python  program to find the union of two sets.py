def find_set_union(set1, set2):
  """
  Calculates the union of two sets.

  Args:
    set1: The first set.
    set2: The second set.

  Returns:
    A new set containing all unique elements from both input sets.
  """
  return set1.union(set2)

# Example usage:
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

union_result = find_set_union(set_a, set_b)
print(f"The union of {set_a} and {set_b} is: {union_result}")

# Alternative method using the | operator:
union_with_operator = set_a | set_b
print(f"The union using the '|' operator is: {union_with_operator}")
