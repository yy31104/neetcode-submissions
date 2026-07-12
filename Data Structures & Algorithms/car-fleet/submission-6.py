class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        cars.sort(key=lambda car: car[0], reverse = True)
        for pos,s in cars:
            time = (target - pos) / s
            if not stack or stack[-1] < time:
                stack.append(time)
        return len(stack)