import unittest


class LambdaFunctionTest(unittest.TestCase):
    """
    📝 람다 함수 (Lambda Function) 학습

    람다 함수는 Python에서 한 줄로 간단한 함수를 정의할 때 사용됩니다.
    일반적인 `def` 키워드로 정의하는 함수와는 달리, `lambda` 키워드를 사용하여 작성합니다.

    ✅ 람다 함수 기본 구조:
    lambda 매개변수: 반환값

    ✅ 람다 함수와 일반 함수 비교:
    def add(x, y):
        return x + y

    add_lambda = lambda x, y: x + y
    위의 두 함수는 같은 동작을 합니다.
    """

    def test_lambda_basic(self):
        """ 🏗️ 람다 함수 기본 사용법
        람다 함수를 사용하면 한 줄로 간단한 연산을 수행할 수 있습니다.
        """

        add_two = None  # TODO: `lambda x: x + 2` 형태의 람다 함수를 작성하여 3을 입력하면 5가 반환되도록 만드세요.

        self.assertEqual(add_two(3), 5)

    def test_lambda_with_map(self):
        """ 🏗️ 람다 함수와 `map` 활용
        `map` 함수는 리스트의 각 요소에 대해 특정 연산을 수행하는 함수입니다.
        """

        numbers = [1, 2, 3, 4, 5]
        doubled_numbers = None  # TODO: `map`을 사용하여 리스트의 모든 요소에 2를 곱하는 람다 함수를 적용하세요.

        self.assertEqual(list(doubled_numbers), [2, 4, 6, 8, 10])

    def test_lambda_sort(self):
        """ 🏗️ 람다 함수와 `sorted` 활용
        `sorted` 함수의 `key` 매개변수에 람다 함수를 전달하면 정렬 기준을 정의할 수 있습니다.
        """

        students = [("Alice", 90), ("Bob", 85), ("Charlie", 95)]
        sorted_students = None  # TODO: 두 번째 요소(점수)를 기준으로 정렬하는 람다 함수를 작성하세요.

        self.assertEqual(sorted_students, [("Bob", 85), ("Alice", 90), ("Charlie", 95)])
