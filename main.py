try:
  print("a =", a)
except NameError as e:
  print(e)
finally:
  print("we may omit 'finally'")

print("after the try except block")
