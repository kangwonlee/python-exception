# lp3thw p. 142
# a = 1

try:
  print("a is", a)
  assert False, "무조건 예외 발생"
except NameError as e:
  print(e)
except AssertionError as f:
  print("예외 발생:", f)
finally:
  print("we may omit 'finally'")

print("after the first try except block")


print('=' * 10)
a = 1

try:
  print("a is", a)
  assert False, "무조건 예외 발생"
except NameError as e:
  print(e)
except AssertionError as f:
  print("예외 발생:", f)
finally:
  print("we may omit 'finally'")

print("after the second try except block")


print('=' * 10)
a = 2

try:
  print("a is", a)
  assert False, "무조건 예외 발생"
except NameError as e:
  print(e)
except AssertionError as f:
  print("예외 발생:", f)
  raise f
finally:
  print("we may omit 'finally'")

print("after the third try except block")
