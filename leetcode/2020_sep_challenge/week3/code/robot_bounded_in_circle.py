class Solution:
    def turnLeft(self, direction):
        dir_map = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
        return dir_map[direction]

    def turnRight(self, direction):
        dir_map = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
        return dir_map[direction]

    def move(self, pos, direction):
        if direction == 'N':
            pos[1] += 1
        elif direction == 'W':
            pos[0] -= 1
        elif direction == 'S':
            pos[1] -= 1
        else:
            pos[0] += 1

    def isRobotBounded(self, instructions: str) -> bool:
        direction = 'N'
        pos = [0, 0]
        for ins in instructions:
            if ins == 'G':
                self.move(pos, direction)
            elif ins == 'L':
                direction = self.turnLeft(direction)
            else:
                direction = self.turnRight(direction)
        if direction != 'N' or pos == [0, 0]:
            return True
        return False

