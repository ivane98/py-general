def is_prime(n):
    for i in range(2, int(n**.5 + 1)):
        if n % i == 0:
            return False
    return True

def gap(g, m, n):
    start = 0
    end = 0
    for i in range(m,n):
      if is_prime(i):
        if start == 0:
          start = i
        elif end == 0:
          end = i
        else:
          start = end
          end = i
      if end - start == g:
        return [start, end]
    return None
          


print(gap(6,100,110))