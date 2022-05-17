class MaxHeap:
    #Used to keep track of the 50 most common words

    def __init__(self):
        self.heap = []

    def add(self, pair):
        i = 0

        for i, entry in enumerate(self.heap):
            if pair[1] > entry[1]: break
        
        self.heap.insert(i, pair)

        if len(self.heap) > 50: self.heap = self.heap[:-1]

    def to_dict(self):
        dict = {}

        for entry in self.heap:
            dict[entry[0]] = [entry[1]]

        return dict