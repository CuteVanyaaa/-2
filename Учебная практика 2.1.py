def count_jewels(J, S):
  jewels = set(J)
  count = 0
  for stone in S:
    if stone in jewels:
      count += 1
  return count

J = "ab"
S = "aabbccd"
result = count_jewels(J, S)
print(result)
