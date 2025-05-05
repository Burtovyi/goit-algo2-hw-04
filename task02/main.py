from trie import Trie

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        """
        Знаходить найдовший спільний префікс для всіх слів у списку strings.

        Args:
            strings (list of str): Вхідний масив рядків.

        Returns:
            str: Найдовший спільний префікс.
        """
        # Перевірка коректності вхідних даних
        if not isinstance(strings, list):
            raise TypeError("Input must be a list of strings")
        if len(strings) == 0:
            return ""
        # Всі елементи мають бути рядками
        for s in strings:
            if not isinstance(s, str):
                raise TypeError("All elements in the list must be strings")
        # Ініціалізуємо префікс як перший рядок
        prefix = strings[0]
        # Для кожного наступного рядка звужуємо префікс
        for s in strings[1:]:
            # звужуємо поки s не починається з prefix
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix

if __name__ == "__main__":
    # Тести
    lcp = LongestCommonWord()

    test1 = ["flower", "flow", "flight"]
    assert lcp.find_longest_common_word(test1) == "fl"

    test2 = ["interspecies", "interstellar", "interstate"]
    assert lcp.find_longest_common_word(test2) == "inters"

    test3 = ["dog", "racecar", "car"]
    assert lcp.find_longest_common_word(test3) == ""

    test4 = []
    assert lcp.find_longest_common_word(test4) == ""

    try:
        lcp.find_longest_common_word("not a list")
    except TypeError:
        pass  # очікуємо TypeError
    else:
        raise AssertionError("TypeError not raised for non-list input")

    try:
        lcp.find_longest_common_word(["ok", 123])
    except TypeError:
        pass  # очікуємо TypeError
    else:
        raise AssertionError("TypeError not raised for non-str element")

    print("All tests passed!")
