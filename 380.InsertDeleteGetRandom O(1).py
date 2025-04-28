'''
Link: https://leetcode.com/problems/insert-delete-getrandom-o1
'''

import random
class RandomizedSet:

    def __init__(self):
        self.data, self.pos = [], {}

    def insert(self, val: int) -> bool:
        if val not in self.pos:
            self.data.append(val)
            self.pos[val] = len(self.data) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.pos:
            idx, last = self.pos[val], self.data[-1]
            self.data[idx] = last
            self.pos[last] = idx
            self.data.pop()
            self.pos.pop(val, 0)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()