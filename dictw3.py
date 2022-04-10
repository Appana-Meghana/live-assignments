dictionary1 = {'reptiles':'sanke','mammals':'whale','amphibians':'frogs'}
list1 = ['tiger', 'lion']
dictionary1_copy = dictionary1.copy()
list1.append(dictionary1_copy)
print('dict in list:',list1)

myDictionary = {}
myDictionary["key1"] = [1, 2]
list = ['a','b','c']
myDictionary["key1"].append(list)
print('list in dict:',myDictionary)
