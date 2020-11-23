from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        conversion = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        unique = set()
        for word in words:
            unique.add("".join([conversion[ord(ch) - ord('a')] for ch in word]))
        return len(unique)
