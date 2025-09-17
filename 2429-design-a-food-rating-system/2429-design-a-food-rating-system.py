class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisines_to_foods=defaultdict(list)
        self.foods_to_ratings={}
        self.foods_to_cuisines={}

        for f,c,r in zip(foods,cuisines,ratings):
            self.foods_to_ratings[f]=r
            self.foods_to_cuisines[f]=c
            heappush(self.cuisines_to_foods[c],(-r,f))
            
    def changeRating(self, food: str, newRating: int) -> None:
        self.foods_to_ratings[food]=newRating
        cuisine=self.foods_to_cuisines[food]
        heappush(self.cuisines_to_foods[cuisine],(-newRating,food))


    def highestRated(self, cuisine: str) -> str:
        tmp=self.cuisines_to_foods[cuisine]
        while tmp:
            r,f=tmp[0]
            if self.foods_to_ratings[f]==-r:
                return f
            heappop(tmp)

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)