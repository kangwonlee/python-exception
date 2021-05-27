# lp3thw p. 142
# a = 1

try:
  assert False, "(코드 짠 사람 속이 뒤틀렸는지) 무조건 예외 발생~~"
  print("a is", a)
except NameError as e:
  print(e)
except AssertionError as f:
  print("예외 발생:", f)
  # raise f
finally:
  print("we may omit 'finally'")

print("after the try except block")
