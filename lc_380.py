class RandomizedSet(object):

    def __init__(self):
        self.val_map = {}
        self.val_list = []

    def insert(self, val):
        if val in self.val_map:
            return False

        self.val_map[val] = len(self.val_list)
        self.val_list.append(val)
        return True

    def remove(self, val):
        if val not in self.val_list:
            return False
        
        index = self.val_map[val]
        last = self.val_list[-1]
        self.val_list[index] = last
        self.val_list.pop()
        self.val_map[last] = index
        del self.val_map[val]
        return True


    def getRandom(self):
        return random.choice(self.val_list)


obj = RandomizedSet()

param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_3 = obj.getRandom()

print(param_1, param_2, param_3)
