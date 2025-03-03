import unittest

class TypeConversionTest(unittest.TestCase):
    """ 🎯 형변환(자료형 변환)
    프로그래밍에서는 다양한 데이터 타입이 존재합니다.
    - 정수(`int`)
    - 실수(`float`)
    - 문자열(`str`)
    데이터 타입이 다르면 연산이 불가능한 경우가 많으므로 형변환(type conversion)이 필요합니다.
    이 단원에서는 Python에서 자주 사용되는 형변환을 학습합니다.
    """

    def test_정수를_문자열로_변환(self):
        """ 🔄 `int` → `str` 변환 """
        number = 123
        # TODO: number를 문자열로 변환하세요.
        result = None  # 여기를 수정하세요
        self.assertEqual(result, "123")

    def test_문자열을_정수로_변환(self):
        """ 🔄 `str` → `int` 변환 """
        text = "456"
        # TODO: text를 정수형으로 변환하세요.
        result = None  # 여기를 수정하세요
        self.assertEqual(result, 456)

    def test_문자열을_실수로_변환(self):
        """ 🔄 `str` → `float` 변환 """
        text = "3.14"
        # TODO: text를 실수형으로 변환하세요.
        result = None  # 여기를 수정하세요
        self.assertEqual(result, 3.14)

    def test_실수를_정수로_변환(self):
        """ 🔄 `float` → `int` 변환 (소수점 제거) """
        number = 9.99
        # TODO: number를 정수형으로 변환하세요.
        result = None  # 여기를 수정하세요
        self.assertEqual(result, 9)

    def test_정수와_문자열을_연결하기(self):
        """ 🔄 정수 + 문자열을 `str`로 변환하여 연결 """
        age = 25
        name = "Alice"
        # TODO: age를 문자열로 변환하여 name과 연결하세요. Hint -> fString 이라는 키워드에 대해 검색해보시는것을 추천합니다.
        result = None
        self.assertEqual(result, "Alice is 25 years old.")

if __name__ == "__main__":
    unittest.main()
