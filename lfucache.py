class LFUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = {}
        self.counter = {}
        self.curr_time = 0
        self.low_key = None

    def get(self, key):
        self.curr_time += 1
        if key in self.storage:
            val = int(self.storage[key].split('|')[0])
            self.counter[key] += 1
            self.storage[key] = str(val) + '|' + str(self.curr_time)
            return val

        return -1

    def set(self, key, value):
        self.curr_time += 1
        if self.low_key is None:
            self.low_key = key

        if len(self.storage.keys()) >= self.capacity:
            # evict least frequently used item
            low = int(self.counter[self.low_key])
            last_used_time = int(self.storage[self.low_key].split('|')[1])

            for curr_key in self.counter:
                if self.counter[curr_key] < low:
                    low = self.counter[curr_key]
                    self.low_key = curr_key

                elif low == self.counter[curr_key]:
                    if int(self.storage[curr_key].split('|')[1]) < last_used_time:
                        self.low_key = curr_key


            self.storage.pop(self.low_key)
            self.counter.pop(self.low_key)
            self.low_key = key

        self.storage[key] = str(value) + '|' + str(self.curr_time)
        self.counter[key] = 0

cache = LFUCache(2)

cache.set(2,1)
cache.set(1,1)
cache.set(2,3)
cache.set(4,1)
cache.get(1)
cache.get(2)

# cache.set(1, 1)
# cache.set(2, 2)
# cache.get(1)       # returns 1
# cache.set(3, 3);    # evicts key 2
# cache.get(2);       # returns -1 (not found)
# cache.get(3);       # returns 3.
# cache.set(4, 4);    # evicts key 1.
# cache.get(1);       # returns -1 (not found)
# cache.get(3);       # returns 3
# cache.get(4);       # returns 4