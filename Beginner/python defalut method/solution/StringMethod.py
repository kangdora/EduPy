import unittest

class StringMethod(unittest.TestCase):
    """
    📝 문자열(String) 기본 메서드 테스트

    문자열의 주요 메서드를 학습하는 단원입니다.

    중요도
    0️⃣1️⃣ strip ⭐⭐⭐
    0️⃣2️⃣ split ⭐⭐⭐
    0️⃣3️⃣ join ⭐⭐⭐
    0️⃣4️⃣ replace ⭐⭐✩
    0️⃣5️⃣ find ⭐⭐✩
    0️⃣6️⃣ count ⭐⭐✩
    0️⃣7️⃣ startswith / endswith ⭐⭐✩
    0️⃣8️⃣ upper / lower ⭐✰✰
    0️⃣9️⃣ zfill ⭐✰✰ (안다름)
    1️⃣0️⃣ isnumeric / isdigit ⭐✰✰ (안다름)

    문자열은 변경 불가능(immutable)한 자료형입니다.
    따라서 모든 문자열 메서드는 원본을 수정하지 않고 새로운 문자열을 반환합니다.
    """

    def test_strip(self):
        """ 🏗️ strip
        문자열 앞뒤의 공백 또는 특정 문자를 제거합니다.
        """

        text = "  hello world  "

        stripped = text.strip()

        self.assertEqual(stripped, "hello world")

    def test_split(self):
        """ 🏗️ split
        특정 구분자로 문자열을 분리합니다.
        """

        text = "apple,banana,grape"

        words = text.split(",")

        self.assertEqual(words, ["apple", "banana", "grape"])

    def test_join(self):
        """ 🏗️ join
        리스트의 문자열을 하나의 문자열로 결합합니다.
        """

        words = ["Hello", "world"]

        sentence = " ".join(words)

        self.assertEqual(sentence, "Hello world")

    def test_replace(self):
        """ 🏗️ replace
        문자열에서 특정 부분을 다른 문자열로 변경합니다.
        """

        text = "I love Python"

        new_text = text.replace("love", "like")

        self.assertEqual(new_text, "I like Python")

    def test_find(self):
        """ 🏗️ find
        특정 문자열의 첫 등장 위치를 찾습니다. 없으면 -1을 반환합니다.
        """

        text = "Hello world"

        position = text.find("world")

        self.assertEqual(position, 6)

        not_found = text.find("Python")

        self.assertEqual(not_found, -1)

    def test_count(self):
        """ 🏗️ count
        특정 문자열이 등장하는 횟수를 반환합니다.
        """

        text = "banana banana banana"

        count = text.count("banana")

        self.assertEqual(count, 3)

    def test_startswith_and_endswith(self):
        """ 🏗️ startswith / endswith
        특정 문자열로 시작하는지 또는 끝나는지를 확인합니다.
        """

        text = "hello.py"

        ends_with_py = text.endswith(".py")

        starts_with_hello = text.startswith("hello")

        self.assertTrue(ends_with_py)
        self.assertTrue(starts_with_hello)

    def test_upper_and_lower(self):
        """ 🏗️ upper / lower
        문자열의 대소문자를 변환합니다.
        """

        text = "Python"

        upper_text = text.upper()

        lower_text = text.lower()

        self.assertEqual(upper_text, "PYTHON")
        self.assertEqual(lower_text, "python")
