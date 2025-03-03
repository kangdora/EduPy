import unittest

class ConditionalStatementsTest(unittest.TestCase):
    """ 🎯 조건문 (if, elif, else)
    조건문은 특정 조건에 따라 프로그램의 실행 흐름을 제어하는 기능을 합니다.
    Python에서는 다음과 같은 연산자를 활용할 수 있습니다.
    - `==` : 같음
    - `!=` : 다름
    - `>`  : 크다
    - `<`  : 작다
    - `>=` : 크거나 같다
    - `<=` : 작거나 같다
    - `and` : 논리곱 (모두 참일 때 참)
    - `or`  : 논리합 (하나라도 참이면 참)
    """

    def test_같은지_비교하기(self):
        """ ✅ `==` 연산자를 사용하여 두 값이 같은지 비교 """
        a, b = 5, 5
        result = (a == b)
        self.assertEqual(result, True)

    def test_다른지_비교하기(self):
        """ ❌ `!=` 연산자를 사용하여 두 값이 다른지 비교 """
        a, b = 3, 7
        result = (a != b)
        self.assertEqual(result, True)

    def test_크거나_같은지_비교하기(self):
        """ 🔼 `>=` 연산자를 사용하여 크거나 같은지 비교 """
        a, b = 10, 7
        result = (a >= b)
        self.assertEqual(result, True)

    def test_작거나_같은지_비교하기(self):
        """ 🔽 `<=` 연산자를 사용하여 작거나 같은지 비교 """
        a, b = 4, 8
        result = (a <= b)
        self.assertEqual(result, True)

    def test_and_연산자(self):
        """ 🔗 `and` 연산자를 사용하여 두 조건이 모두 참인지 확인 """
        a, b = 6, 12
        result = (a > 5 and b > 10)
        self.assertEqual(result, True)

    def test_or_연산자(self):
        """ 🔗 `or` 연산자를 사용하여 하나라도 참인지 확인 """
        a, b = 4, 15
        result = (a > 5 or b > 10)
        self.assertEqual(result, True)

    def test_if_else(self):
        """ 🛤️ `if-else` 문을 활용한 흐름 제어 """
        age = 20
        # 이 방식도 있지만
        if (age >= 18):
            result = "성인"
        else:
            result = "미성년자"
        result = "성인" if age >= 18 else "미성년자" # 이런 방식도 가능합니다
        self.assertEqual(result, "성인")

    def test_elif(self):
        """ 🚦 `if-elif-else` 문을 활용하여 여러 조건 처리 """
        score = 85

        # 이또한 이런 방법도 있지만
        if score >= 90:
            result = "A"
        elif score >= 80:
            result = "B"
        elif score >= 70:
            result = "C"
        else:
            result = "F"
        result = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F" # 이 방식도 가능합니다
        self.assertEqual(result, "B")

if __name__ == "__main__":
    unittest.main()
