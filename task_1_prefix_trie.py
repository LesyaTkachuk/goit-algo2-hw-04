from trie import Trie

class PrefixSuffixTrie(Trie):
    def count_words_with_suffix(self, pattern)->int:
        if not isinstance(pattern, str):
            raise TypeError(f"Illegal argument for countWordsWithPrefix: prefix = {pattern} must be a string")
        
        all_words = self.keys()
        count = 0
        for word in all_words:
            if word.endswith(pattern):
                count += 1
        return count
                       
    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise TypeError(f"Illegal argument for countWordsWithPrefix: prefix = {prefix} must be a string")
        
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True

if __name__ == '__main__':
    prefix_suffix_trie = PrefixSuffixTrie()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        prefix_suffix_trie.put(word, i)

    # check the number of words ending with a given suffix
    assert prefix_suffix_trie.count_words_with_suffix("e") == 1  # apple
    assert prefix_suffix_trie.count_words_with_suffix("ion") == 1  # application
    assert prefix_suffix_trie.count_words_with_suffix("a") == 1  # banana
    assert prefix_suffix_trie.count_words_with_suffix("at") == 1  # cat

    # check if word includes a given prefix
    assert prefix_suffix_trie.has_prefix("app") == True  # apple, application
    assert prefix_suffix_trie.has_prefix("bat") == False
    assert prefix_suffix_trie.has_prefix("ban") == True  # banana
    assert prefix_suffix_trie.has_prefix("ca") == True  # cat
