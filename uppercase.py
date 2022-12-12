def to_uppercase(string):
  upper_count = 0
  for i in range(4):
    if string[i].isupper():
      upper_count += 1
  
  if upper_count >= 2:
    return string.upper()
  else:
    return string


print(to_uppercase("Hello wORld"))