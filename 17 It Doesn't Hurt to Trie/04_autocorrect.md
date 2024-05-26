# Chapter 17

## Exercise 04

Write an autocorrect function that attempts to replace a user's typo with a correct word. The function should accept a string that represents text a user typed in. If the user's string is not in the trie, the function should return an alternative word that shares the longest possible prefix with the user's string

```{r}
def autocorrect(self, word):
    current_node = self.root
    in_trie = ""
    for char in word:
        if current_node.children.get(char):
            in_trie += char
            current_node = current_node.children.get(char)
        else:
            return in_trie + self.collectAllWords([], current_node)[0]
    return word
```