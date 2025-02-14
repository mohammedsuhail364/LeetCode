class ProductOfNumbers:

    def __init__(self):
        self.data=[]
        self.product=1
        

    def add(self, num: int) -> None:
        if num!=0:
            self.product*=num
            self.data.append(self.product)
        else:
            self.product=1
            self.data=[]
        
    def getProduct(self, k: int) -> int:
        if len(self.data)<k: 
            return 0
        if len(self.data)==k:
            return self.data[-1]
        return self.data[-1]//self.data[-k-1]

        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)