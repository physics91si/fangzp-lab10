# Constructs a Set class: collection of arbitrary non-repeated objects

class Set(set):
    def __init__(self, set):
        checked = []
        for i in set:
            if i not in checked:
                checked.append(i)
        self.set = checked
    def contains(self, other): # Checks if element is in set
        if other in self.set:
            return "The set contains %s" %other
        else:
            return "The set does not contain %s" %other
    def __add__(self, other): # Add element to set
        return self.set.append(other)
    def remove(self, other): # Removes element from the set
        newset = []
        for i in self.set:
            if i != other:
                newset.append(i)
        return newset
    def size(self): #Returns number of elements in set
        return len(self.set)
    def __union__(self, other): # Union of two sets
        return self.set|other
    def __intersection__(self, other): # Intersection of two sets
        return self.set&other
    def __sub__self(self, other): # Difference of two sets
        diff = []
        for i in self.set:
            if i not in other:
                diff.append(i)
        return diff