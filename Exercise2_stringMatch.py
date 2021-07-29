def StringMatch(s1, s2):
      n = len(s1)
      pos = [1] + [0] * n
      prev = pos[:]
      for i in range(len(s2)):
          preprev = prev
          prev = pos
          pos = [0] * (n + 1)
          if s2[i] == '*':
              for j in range(n + 1):
                  if preprev[j]:
                      pos[j] = 1
                      k = j + 1
                      while k < n + 1 and s2[i - 1] in ('.', s1[k - 1]):
                          pos[k] = 1
                          k += 1
          else:
              for j in range(n):
                  if prev[j]:
                      pos[j + 1] = s2[i] in ('.', s1[j])
      return pos[-1]

def test_cases(string1, string2):
    if StringMatch(string1, string2):
        return True
    else:
        return False


print(test_cases("aba", "*ab"))
print(test_cases("aa", "a*"))
print(test_cases("ab", ".*"))
print(test_cases("ab", "."))
print(test_cases("aab", "c*a*b"))
print(test_cases("aaaa","a*"))
print(test_cases("abaa","ab.*"))