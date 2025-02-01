from trie import Trie
from collections import defaultdict

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings)->str:
        for word in strings:
            if not self.contains(word):
                self.put(word)
        current_node = self.root
        prefix = []

        for char in strings[0]:
            if char in current_node.children:
                if all(word.startswith("".join(prefix)+char) for word in strings):
                    prefix.append(char)
                    current_node = current_node.children[char]
                else:
                    break
            else:
                break

        return "".join(prefix)



if __name__ == '__main__':
    # tests
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""