import sets

MySet=sets.Set([1, 3, 4, 5, 3])
AlsoMySet = sets.Set([3])
print MySet
print AlsoMySet
print MySet.contains(4)
print MySet.__add__(2)
print MySet.remove(3)
print MySet.size()
print MySet.__union__(AlsoMySet)
print MySet.__intersection__(AlsoMySet)
print MySet.__sub__(AlsoMySet)
