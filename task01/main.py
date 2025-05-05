from trie import Trie

class Homework(Trie):
    def __init__(self):
        super().__init__()
        # Для швидкого доступу до всіх слів у методах суфікса/префікса
        self._words = []

    def put(self, key, value):
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        # Додаємо в базове Trie
        super().put(key, value)
        # Записуємо в список слів
        self._words.append(key)

    def count_words_with_suffix(self, pattern) -> int:
        """
        Повертає кількість слів, що закінчуються на заданий шаблон `pattern`.
        """
        if not isinstance(pattern, str):
            raise TypeError("Pattern must be a string")
        # Рахуємо слова зі списку _words
        return sum(1 for w in self._words if w.endswith(pattern))

    def has_prefix(self, prefix) -> bool:
        """
        Повертає True, якщо існує хоча б одне слово із заданим префіксом `prefix`.
        """
        if not isinstance(prefix, str):
            raise TypeError("Prefix must be a string")
        # Шукаємо в списку _words
        return any(w.startswith(prefix) for w in self._words)


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1   # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1   # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Перевірка наявності префікса
    assert trie.has_prefix("app") is True   # apple, application
    assert trie.has_prefix("bat") is False
    assert trie.has_prefix("ban") is True   # banana
    assert trie.has_prefix("ca") is True    # cat

    print("All tests passed!")
