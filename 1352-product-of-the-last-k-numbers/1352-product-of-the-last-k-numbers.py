class ProductOfNumbers:

    def __init__(self):
        self.nums=[]
        self.product = 1
    def add(self, num: int) -> None:
        if num!=0:
            self.product*=num
            self.nums.append(self.product)
        else:
            self.product=1
            self.nums=[]

    def getProduct(self, k: int) -> int:
        if len(self.nums)<k:return 0
        if len(self.nums)==k:return self.nums[-1]
        return self.nums[-1]//self.nums[-k-1]
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
