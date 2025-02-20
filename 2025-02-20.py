class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        x = 0
        y = 0
        for cmd in commands:
            match cmd:
                case "UP":
                    y -= 1
                case "DOWN":
                    y += 1
                case "RIGHT":
                    x += 1
                case "LEFT":
                    x -= 1
        return y*n + x