def duplicate(list: int) -> bool:
  for i in range(10):
    for j in range(10):
      if i != j:
        if list[i] == list[j]:
          return True
  return False      

list = [1,2,3,4,5,6,7,8,9,1]
print(f"Duplicate found: {duplicate(list)}")
