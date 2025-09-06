import unittest


class DictMethod(unittest.TestCase):
    """
    📝 딕셔너리 기본 메서드 테스트

    딕셔너리의 메서드들을 학습하기 위한 단원입니다.

    중요도
    0️⃣1️⃣ copy ⭐⭐✩
    0️⃣2️⃣ pop ⭐✰ ✰
    0️⃣3️⃣ values ⭐⭐✩
    0️⃣4️⃣ get ⭐⭐⭐
    0️⃣5️⃣ keys ⭐⭐✩
    0️⃣6️⃣ clear ⭐✰ ✰
    0️⃣7️⃣ fromkeys ⭐✰ ✰
    0️⃣8️⃣ items ⭐⭐✩
    0️⃣9️⃣ popitem ⭐✰ ✰
    1️⃣0️⃣ setdefault ⭐⭐⭐
    1️⃣1️⃣ update ⭐⭐✩

    딕셔너리는 key:value 형태로 제공되는 자료구조입니다. 공통적으로 해시맵, 맵이라고 불리며, 특징으로는 특정 원소를 바로 찾을 수 있습니다.
    순서가 보장되는 자료구조는 아니었으나 3.7버전부터 순서가 보장되어, popitem()을 사용할 수 있게 되었습니다.
    """


    def test_dict_copy(self):
        """ 🏗️ copy
        딕셔너리의 얕은 복사를 수행합니다.
        """

        original = {"a": 1, "b": 2}

        copied = None  # TODO: 딕셔너리를 복사하세요.

        self.assertEqual(copied, original)
        self.assertIsNot(copied, original)  # 서로 다른 객체여야 함

    def test_dict_pop(self):
        """ 🏗️ pop
        특정 키의 값을 제거하고 반환합니다.
        """

        data = {"x": 10, "y": 20, "z": 30}

        removed_value = None  # TODO: 키 "y"의 값을 제거하세요.

        self.assertEqual(removed_value, 20)
        self.assertNotIn("y", data)

    def test_dict_values(self):
        """ 🏗️ values
        딕셔너리의 모든 값을 반환합니다.
        """

        data = {"a": 1, "b": 2, "c": 3}

        values = None  # TODO: 딕셔너리의 값들을 가져오세요.

        self.assertEqual(values, [1, 2, 3])

    def test_dict_get(self):
        """ 🏗️ get
        특정 키의 값을 가져오며, 키가 없으면 기본값을 반환할 수 있습니다.
        """

        data = {"name": "Alice", "age": 25}

        name = None  # TODO: 키 "name"의 값을 가져오세요.

        # 존재하지 않는 키의 기본값은 이렇게 가져옵니다.
        country = data.get("country", "Unknown")

        self.assertEqual(name, "Alice")
        self.assertEqual(country, "Unknown")

    def test_dict_keys(self):
        """ 🏗️ keys
        딕셔너리의 모든 키를 반환합니다.
        """

        data = {"x": 10, "y": 20, "z": 30}

        keys = None  # TODO: 딕셔너리의 키들을 가져와서 리스트 형태로 묶어주세요.

        self.assertEqual(keys, ["x", "y", "z"])

    def test_dict_clear(self):
        """ 🏗️ clear
        딕셔너리의 모든 요소를 제거합니다.
        """

        data = {"a": 1, "b": 2}

        # TODO: 딕셔너리를 비우세요.

        self.assertEqual(data, {})

    def test_dict_items(self):
        """ 🏗️ items
        딕셔너리의 모든 키-값 쌍을 반환합니다.
        """

        data = {"a": 1, "b": 2, "c": 3}

        items = None  # TODO: 키-값 쌍을 가져와서 리스트 형태로 묶어주세요

        self.assertEqual(items, [("a", 1), ("b", 2), ("c", 3)])

    def test_dict_popitem(self):
        """ 🏗️ popitem
        마지막 키-값 쌍을 제거하고 반환합니다.
        """

        data = {"x": 10, "y": 20}

        popped = None  # TODO: 마지막 요소를 제거하세요.

        self.assertEqual(popped, ("y", 20))
        self.assertEqual(len(data), 1)

    def test_dict_setdefault(self):
        """ 🏗️ setdefault
        키가 없으면 기본값을 설정하고 반환합니다.
        """

        data = {"name": "Alice"}

        age = None   # TODO: 딕셔너리의 "age" 키가 없을 때 기본값 30을 설정하세요.

        self.assertEqual(age, 30)
        self.assertEqual(data, {"name": "Alice", "age": 30})
