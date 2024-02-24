import typing as t


class Trie:
    def __init__(self) -> None:  # O(1)
        self.root = Trie.Node()

    class Node:
        def __init__(self) -> None:  # O(1)
            self.children: t.Dict[str, "Trie.Node"] = {}
            self.is_end_of_word: bool = False

    def insert(self, word: str) -> None:  # O(n)
        current = self.root
        for char in word:  # O(n)
            if char not in current.children:
                current.children[char] = Trie.Node()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word: str) -> bool:  # O(n)
        current = self.root
        for char in word:  # O(n)
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def __str__(self) -> str:
        if not self.root.children:
            return

        queue = [self.root]
        result = ""
        while queue:
            current = queue.pop(0)
            for key, value in current.children.items():
                result += key
                queue.append(value)
        return result


def delete(root: Trie.Node, word: str, index: int) -> bool:  # O(n)
    """
    Deletion of a word from a trie
    case1: some other prefix of string is same as the one that we want to delete ex) API, APPlE
    case2: The string is a prefix of another string ex) API, APIS
    case3: Other string is a prefix of this string ex) APIS, AP
    case4: Not any node depends on this String ex) APIS, K
    """
    ch = word[index]
    current = root.children.get(ch)
    can_delete_node = False

    if len(current.children) > 1:  # if there are more than 1 children (for case1)
        delete(current, word, index + 1)
        return False

    last_index = len(word) - 1
    if index == last_index:  # if last character of the word (for case2)
        if len(current.children) >= 1:  # if current node has children (for case3)
            current.is_end_of_word = False
            return False
        else:
            root.children.pop(ch)
            return True

    if current.is_end_of_word == True:  # if current node is end of word (for case3)
        delete(current, word, index + 1)
        return False  # need to return False to tell the parent node that we can't delete the current node

    can_delete_node = delete(current, word, index + 1)  # usual case
    if can_delete_node:
        root.children.pop(ch)
        return True
    else:
        return False


trie = Trie()
trie.insert("hello")
trie.insert("helium")
delete(trie.root, "helium", 0)
print(trie)
