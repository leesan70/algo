from collections import deque
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        got_through = []
        stack = deque()
        for a in asteroids:
            # Left heading
            if a < 0:
                even = False
                while stack:
                    right_heading = stack.pop()
                    # Right heading is bigger. Add back to stack
                    if right_heading > -a:
                        stack.append(right_heading)
                        break
                    # Both exploded. Keep even as a flag for special case
                    elif right_heading == -a:
                        even = True
                        break
                # Add left heading to got through unless left also exploded
                if not stack and not even:
                    got_through.append(a)
            # Simply add to the stack if right heading
            else:
                stack.append(a)
        got_through.extend(list(stack))
        return got_through
