class Solution:
    def wordPattern(self, pattern: str, strr: str) -> bool:
        split_words = strr.split(" ")
        pattern_to_word_list = [None for _ in range(ord('z') - ord('a'))]
        word_to_pattern_dict = {}
        if len(split_words) != len(pattern):
            return False

        for i in range(len(pattern)):
            curr_word = split_words[i]
            curr_pattern = pattern[i]
            curr_pattern_ord = ord(curr_pattern) - ord('a')
            stored_word = pattern_to_word_list[curr_pattern_ord]

            if curr_word in word_to_pattern_dict:
                if word_to_pattern_dict[curr_word] != curr_pattern:
                    return False
            elif stored_word is not None:
                if stored_word != curr_word:
                    return False
            else:
                pattern_to_word_list[curr_pattern_ord] = curr_word
                word_to_pattern_dict[curr_word] = curr_pattern
        return True
