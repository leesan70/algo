class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_split = list(map(int, version1.split(".")))
        version2_split = list(map(int, version2.split(".")))
        len_diff = abs(len(version1_split) - len(version2_split))
        if len(version1_split) > len(version2_split):
            version2_split.extend([0 for _ in range(len_diff)])
        elif len(version2_split) > len(version1_split):
            version1_split.extend([0 for _ in range(len_diff)])
        for num1, num2 in zip(version1_split, version2_split):
            if num1 > num2:
                return 1
            elif num2 > num1:
                return -1
        return 0
