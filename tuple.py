tuple1=(10,20,30,40,50,60)
list1=list(tuple1)
print('original list=',list1)
list1.append(100)
tuple1=tuple(list1)
print('new list=',tuple1)
