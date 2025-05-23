def combinationSum2(candidates, target):
  result = []
  candidates.sort()

  def backtrack(combination, remaining, start):
    if remaining == 0:
      result.append(combination.copy())
      return
    if remaining < 0:
      return

    for i in range(start, len(candidates)):
      if i > start and candidates[i] == candidates[i - 1]:
        continue

      combination.append(candidates[i])
      backtrack(combination, remaining - candidates[i], i + 1)
      combination.pop()

  backtrack([], target, 0)
  return result

candidates1 = [2, 5, 2, 1, 2]
target1 = 5
result1 = combinationSum2(candidates1, target1)
print(result1)
