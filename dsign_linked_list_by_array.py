class MyArrayList:
    # 默认初始容量
    INIT_CAP = 1

    def __init__(self, init_capacity=None):
        self.data = [None]
        self.size = 0

    # add
    def add_last(self, e):
        cap = len(self.data)
        if self.size == cap:
            self._resize(2 * cap)
        self.data[self.size] = e
        self.size += 1
        