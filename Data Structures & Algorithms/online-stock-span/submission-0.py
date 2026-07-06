class StockSpanner:

    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        self.arr.append(price)
        count = 0
        for p in range(len(self.arr) - 1, -1, -1):
            if self.arr[p] <= price:
                count += 1
            else:
                break
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)