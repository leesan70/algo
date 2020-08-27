def till_one(n, k):
  count = 0
  while n > 1:
    leftover = n % k
    if leftover != 0:
      if n - leftover > 1:
        count += leftover
        n -= leftover
      else:
        count += leftover - 1
        n = 1
    else:
      count += 1
      n = n // k
  return count