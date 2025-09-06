import unittest


class DictAndSetTest(unittest.TestCase):
    """ 🗂️ 딕셔너리(`dict`)와 집합(`set`)

    🔹 딕셔너리(`dict`)란?
       키(Key)와 값(Value)로 이루어진 자료구조입니다.
       다른 언어와 비교
         - Python: `{"name": "Alice", "age": 25}`
         - JavaScript: `{ "name": "Alice", "age": 25 }` (Object, Map)
         - Java: `Map<String, Integer> map = new HashMap<>();`
         - C++: `std::unordered_map<std::string, int> map;`

       ✅ 딕셔너리 기본 문법
         my_dict = {"name": "Alice", "age": 25}
         value = my_dict["name"]  # "Alice"

    🔹 **집합(`set`)이란?
       중복을 허용하지 않는 자료구조입니다.
       다른 언어와 비교
         - Python: `{1, 2, 3}`
         - JavaScript: `new Set([1, 2, 3])`
         - Java: `Set<Integer> set = new HashSet<>();`
         - C++: `std::unordered_set<int> set;`

       ✅ 집합 기본 문법
         my_set = {1, 2, 3}
         my_set.add(4)  # {1, 2, 3, 4}
    """

    def test_딕셔너리_기본_사용법(self):
        """ 🔑 `dict` 기본 사용법 """
        # TODO: 이름(name)이 "Alice"이고, 나이(age)가 25인 딕셔너리를 생성하세요.
        my_dict = None  # 이 부분을 수정하세요

        self.assertEqual(my_dict["name"], "Alice")
        self.assertEqual(my_dict["age"], 25)

    def test_딕셔너리_새로운_키_추가(self):
        """ ➕ `dict`에 새로운 키-값 추가하기 """
        my_dict = {"name": "Alice"}
        # TODO: "age" 키를 추가하고 값으로 25를 저장하세요.

        self.assertEqual(my_dict["age"], 25)

    def test_딕셔너리_키_존재_확인(self):
        """ 🔍 `dict`에서 특정 키가 존재하는지 확인하기 """
        my_dict = {"name": "Alice", "age": 25}
        # TODO: "name" 키가 존재하면 True를 반환하세요.
        result = None  # 이 부분을 수정하세요

        self.assertEqual(result, True)

    def test_집합_기본_사용법(self):
        """ 🔢 `set` 기본 사용법 """
        # TODO: 1, 2, 3을 포함하는 집합을 생성하세요.
        my_set = None  # 이 부분을 수정하세요

        self.assertEqual(my_set, {1, 2, 3})

    def test_집합_요소_추가(self):
        """ ➕ `set`에 새로운 요소 추가하기 """
        my_set = {1, 2, 3}
        # TODO: 4를 추가하세요.

        self.assertEqual(my_set, {1, 2, 3, 4})

    def test_집합_중복_제거(self):
        """ ❌ `set`의 중복 제거 기능 확인 """
        my_set = {1, 2, 2, 3, 3, 3}
        # TODO: my_set을 수정하지 않고 중복이 자동으로 제거되는지 확인하세요.

        self.assertEqual(my_set, {1, 2, 3})


if __name__ == "__main__":
    unittest.main()
