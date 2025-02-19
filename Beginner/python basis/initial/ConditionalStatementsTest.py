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
        # TODO: a와 b가 같다면 True를 반환하도록 result를 수정하세요.
        result = None  # 여기를 수정하세요
        self.assertEqual(result, True)

    def test_다른지_비교하기(self):
        """ ❌ `!=` 연산자를 사용하여 두 값이 다른지 비교 """
        a, b = 3, 7
        # TODO: a와 b가 다르면 True를 반환하도록 result를 수정하세요.
        result = None  # 여기를 수정하세요
        self.assertEqual(result, True)

    def test_크거나_같은지_비교하기(self):
        """ 🔼 `>=` 연산자를 사용하여 크거나 같은지 비교 """
        a, b = 10, 7
        # TODO: a가 b보다 크거나 같다면 True를 반환하도록 수정하세요.
        result = None  # 여기를 수정하세요
        self.assertEqual(result, True)

    def test_작거나_같은지_비교하기(self):
        """ 🔽 `<=` 연산자를 사용하여 작거나 같은지 비교 """
        a, b = 4, 8
        # TODO: a가 b보다 작거나 같다면 True를 반환하도록 수정하세요.
        result = None  # 여기를 수정하세요
        self.assertEqual(result, True)

    def test_and_연산자(self):
        """ 🔗 `and` 연산자를 사용하여 두 조건이 모두 참인지 확인 """
        a, b = 6, 12
        # TODO: a가 5보다 크고, b가 10보다 크다면 True 반환
        result = None  # 여기를 수정하세요
        self.assertEqual(result, True)

    def test_or_연산자(self):
        """ 🔗 `or` 연산자를 사용하여 하나라도 참인지 확인 """
        a, b = 4, 15
        # TODO: a가 5보다 크거나, b가 10보다 크다면 True 반환
        result = None  # 여기를 수정하세요
        self.assertEqual(result, True)

    def test_if_else(self):
        """ 🛤️ `if-else` 문을 활용한 흐름 제어 """
        age = 20
        # TODO: age가 18 이상이면 "성인", 그렇지 않으면 "미성년자"를 반환하세요.
        result = None  # 여기를 수정하세요
        self.assertEqual(result, "성인")

    def test_elif(self):
        """ 🚦 `if-elif-else` 문을 활용하여 여러 조건 처리 """
        score = 85
        # TODO: 점수에 따라 등급을 반환하세요.
        # 90 이상: "A", 80 이상: "B", 70 이상: "C", 그 외: "F"
        result = None  # 여기를 수정하세요
        self.assertEqual(result, "B")

if __name__ == "__main__":
    unittest.main()
