from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas_less_cost = [g - c for g, c in zip(gas, cost)]
        candidates = [i for i in range(len(gas_less_cost)) if gas_less_cost[i] >= 0]
        if sum(gas_less_cost) < 0:
            return -1
        for i in candidates:
            cumulative = 0
            for j in range(i, len(gas_less_cost)):
                cumulative += gas_less_cost[j]
                if cumulative < 0:
                    break
            else:
                for k in range(i):
                    cumulative += gas_less_cost[k]
                if cumulative < 0:
                    break
            if cumulative >= 0:
                return i
        return -1
