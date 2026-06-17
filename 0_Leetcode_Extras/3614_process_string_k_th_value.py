from string import ascii_lowercase

def process_string(s, k):
  result = []
  n = len(s)
  for i in s:
    if i in ascii_lowercase:
      result.append(i)
    elif i == "*":
      if result:
        result.pop()
    elif i == "#":
      result += result
    elif i == "%":
      result.reverse()
  if len(result) > k:
    return result[k]
  else:
    return "."

s = "cd%#*#"
process_string(s, 3)
