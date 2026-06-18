class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle=(abs((30*hour)-(5.5*minutes)))
        return min(hour_angle,360-hour_angle)