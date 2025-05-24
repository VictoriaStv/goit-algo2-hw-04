from trie import Trie

class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None


class LongestCommonWord(Trie):
    def __init__(self):
        super().__init__()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
            raise TypeError("Input must be a list of strings")

        if not strings:
            return ""

        for word in strings:
            self.insert(word)

        prefix = ""
        node = self.root

        while True:
            if len(node.children) == 1 and node.value is None:
                char = next(iter(node.children))
                prefix += char
                node = node.children[char]
            else:
                break

        return prefix


if __name__ == "__main__":

    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    trie = LongestCommonWord()
    strings = []
    assert trie.find_longest_common_word(strings) == ""

    print("Усі тести пройдено успішно")
