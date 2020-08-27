"""
https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
"""

class RankList:
    def __init__(self):
        self._list = []

    def insert(self, value):
        if not self._list:
            self._list.append(Node(value, 1))
        elif self._list and self._list[-1].value == value:
            self._list[-1].increment_freq()
        else:
            prev_rank = self._list[-1].get_rank()
            self._list.append(Node(value, prev_rank + 1))

    def get_node(self, index):
        try:
            return self._list[index]
        except IndexError as ie:
            print(ie)
            return None

    def search(self, value):
        start = 0
        end = len(self._list) - 1
        mid = (start + end) // 2
        while mid != start:
            mid_node = self.get_node(mid)
            mid_value = mid_node.get_value()
            if value == mid_value:
                return mid_node.get_rank()
            elif value < mid_value:
                start = mid
            else:
                end = mid
            mid = (start + end) // 2
        return self.compare_consec(value, start)

    def compare_consec(self, value, first):
        first_node = self.get_node(first)
        first_value = first_node.get_value()
        first_rank = first_node.get_rank()

        if self.get_size() == 1:
            return 2 if value < first_value else 1

        second_node = self.get_node(first + 1)
        second_value = second_node.get_value()
        second_rank = second_node.get_rank()
        if value >= first_value:
            return first_rank
        elif second_value <= value < first_value:
            return second_rank
        return second_rank + 1

    def get_size(self):
        return len(self._list)

    def __str__(self):
        return "[" + ", ".join([str(node) for node in self._list]) + "]"


class Node:
    def __init__(self, value, rank):
        self.value = value
        self.rank = rank
        self.freq = 1

    def increment_freq(self):
        self.freq += 1

    def get_rank(self):
        return self.rank

    def get_value(self):
        return self.value

    def __str__(self):
        return "{}: R{} F{}".format(self.value, self.rank, self.freq)

def construct_rank_list(scores):
    rl = RankList()
    for value in scores:
        rl.insert(value)
    return rl


if __name__ == "__main__":
    scores = list(map(int, "100 100 50 40 40 20 10".strip().split(" ")))
    alice = list(map(int, "5 25 50 120".strip().split(" ")))
    rl = construct_rank_list(scores)
    for alice_score in alice:
        print(rl.search(alice_score))