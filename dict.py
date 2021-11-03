memo = {}
arr = [1,2,3]
memo[1] = arr
arr.insert(0, 1)
memo[2] = arr
print(memo)
