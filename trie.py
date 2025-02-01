from collections import deque

class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None

    def __str__(self):
        children_str = ", ".join(f"{repr(k)}: {v.__str__()}" for k, v in self.children.items())
        return f"TrieNode(children={{ {children_str} }}, value={repr(self.value)})"
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.size = 0

    def __str__(self):
        return f"Trie(root={self.root}, size={self.size})"

    def put(self, key, value=None):
        if not isinstance(key, str) or not key:
            raise TypeError(f"Illegal argument for put: key = {key} must be a non-empty string")
        
        current = self.root
        for char in key:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        if current.value is None:
            self.size +=1
        current.value = value

    def get(self, key):
        if not isinstance(key, str) or not key:
            raise TypeError(f"Illegal argument for get: key = {key} must be a non-empty string")
        
        current = self.root
        for char in key:
            if char not in current.children:
                return None
            current = current.children[char]
        return current.value
    
    def delete(self, key):
        if not isinstance(key, str) or not key:
            raise TypeError(f"Illegal argument for delete: key = {key} must be a non-empty string")
        
        def _delete(node, key, depth):
            if depth == len(key):
                if node.value is not None:
                    node.value = None
                    self.size -= 1
                    return len(node.children) == 0
                return False
            
            char = key[depth]
            if char in node.children:
                should_delete = _delete(node.children[char], key, depth +1)
                if should_delete:
                    del node.children[char]
                    return len(node.children) ==0 and node.value is None
            return False
        return _delete(self.root, key, 0)
    
    def contains(self, key):
        if not isinstance(key, str) or not key:
            raise TypeError(f"Illegal argument for delete: key = {key} must be a non-empty string")
        
        return self.get(key) is not None
    
    def is_empty(self):
        return self.size == 0
    
    def longest_prefix_of(self, s):
        if not isinstance(s, str) or not s:
            raise TypeError(f"Illegal argument for delete: key = {s} must be a non-empty string")
        
        current = self.root
        longest_prefix = ""
        current_prefix = ""
        for char in s:
            if char in current.children:
                current = current.children[char]
                current_prefix += char
                if current.value is not None:
                    longest_prefix = current_prefix
            else:
                break
        return longest_prefix
    
    def keys_with_prefix(self, prefix):
        if not isinstance(prefix, str) or not prefix:
            raise TypeError(f"Illegal argument for delete: prefix = {prefix} must be a non-empty string")
        
        current = self.root
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]
        result = []
        self._collect(current, list(prefix), result)
        return result
    
    def _collect(self, node, path, result):
        if node.value is not None:
            result.append("".join(path))
        for char, next_node in node.children.items():
            path.append(char)
            self._collect(next_node, path, result)
            path.pop()

    def keys(self):
        result =[]
        self._collect(self.root, [], result)
        return result
    
    def autocomplete(self, prefix):
        return self.keys_with_prefix(prefix)
    
    def count_words_with_prefix(self, prefix):
        if not isinstance(prefix, str):
            raise TypeError(f"Illegal argument for countWordsWithPrefix: prefix = {prefix} must be a string")
        
        current = self.root
        for char in prefix:
            if char not in current.children:
                return 0
            current = current.children[char]
        return self._count_words(current)
    
    def _count_words(self, node):
        count = 1 if node.value is not None else 0
        for child in node.children.values():
            count += self._count_words(child)
        return count
    
    def check_spelling(trie, word):
        if not isinstance(word, str) or not word:
            raise TypeError(f"Illegal argument for contains: key = {word} must be a non-empty string")
    
        message = f"{word} is written correctly" if trie.get(word) else f"{word} is not found in the dictionary"

    def get_corrections(self, word, max_distance=1):
        root = self.root
        queue = deque([(root, "", 0)])
        corrections = []

        while queue:
            current_node, current_word, current_distance = queue.popleft()

            if current_distance > max_distance:
                continue

            if current_node.value is not None and current_distance > 0:
                corrections.append(current_word)

            for char, next_node in current_node.children.items():
                next_distance = current_distance + (0 if char == word[len(current_word)] else 1)
                queue.append((next_node, current_word + char, next_distance))

        return corrections       




if __name__ == '__main__':
    # initialize trie
    trie = Trie()

    # put first word and print trie
    trie.put("cat", 1)
    print("Trie:", trie)

    # add more words
    trie.put("can", 2)
    trie.put("dog", 3)
    trie.put("cats", 4)

    # get a word from a trie
    print("Cat in trie:", trie.get("cat"))
    print("Pet in trie:", trie.get("pet"))

    # delete a word from a trie
    trie.put("apple", 5)
    trie.put("app", 6)
    print("Apple in trie:", trie.get("apple"))
    trie.delete("apple")
    print("Apple in trie:", trie.get("apple"))
    print("App in trie:", trie.get("app"))

    # check if a word is in a trie
    print("Can in trie:", trie.contains("can"))

    # check if a trie is empty
    print("Empty trie:", trie.is_empty())

    # find longest prefix of a string
    print("Longest prefix of 'applause':", trie.longest_prefix_of("applause"))
    print("Longest prefix of 'dog':", trie.longest_prefix_of("dog"))

    # find all words with a given prefix
    trie.put("apple", 7)
    trie.put("applause", 8)
    trie.put("appetizer", 9)
    print("Words with prefix 'app':", trie.keys_with_prefix("app"))

    # find all words in a trie
    print("All words in trie:", trie.keys())

    # autocomplete a string
    print("Autocomplete 'app':", trie.autocomplete("app"))

    # count words with a given prefix
    print(f"Nnmber of words with prefix 'app': {trie.count_words_with_prefix('app')}")

    # check spelling
    print("Check spelling 'cat':", trie.check_spelling("cat"))
    print("Check spelling 'batman':", trie.check_spelling("batman"))

    # get corrections
    trie.put("bat", 10)
    trie.put("battery", 11)
    print("Get corrections 'battary' max_distance=1:", trie.get_corrections("battary", max_distance=1))
    print("Get corrections 'battary' max_distance=2:", trie.get_corrections("battary", max_distance=2))


