import unittest
from io import StringIO
import sys

class BasicIOTest(unittest.TestCase):
    """ 📝 Python 기초 학습 단원
    파이썬(Python) 은 쉽고 직관적인 문법을 가진 고급 프로그래밍 언어입니다.
    장점으로는 적은 코드로 같은 기능을 구현하기 쉽다라는 장점이 있고, 배우기 쉽습니다.
    특히나 인터프리터 언어의 장점으로 인해 빠르게 테스트가 가능하다는 장점이 있습니다.
    여러분은 이 코드를 작성하면서 얻을 수 있는 여러가지 중에 어떤 것을 얻고자 이 파일을 여신걸까요?
    """

    def test_print_출력하기(self):
        """ print()
        파이썬에서 print는 기초적인 출력함수입니다.
        사람에게 과정과 결과가 중요하듯이 코딩도 과정과 결과과 중요합니다.
        그런데 그 과정과 결과를 확인할 수 없다면 어떻게 될까요?
        그러니 제일 기본 함수인 print()부터 공부해봅시다.
        """
        expected_output = "Hello, Python!"

        original_stdout = sys.stdout
        sys.stdout = StringIO()

        try:
            # TODO: "Hello, Python!" 을 출력해봅시다.
            actual_output = sys.stdout.getvalue().rstrip()
        finally:
            sys.stdout = original_stdout

        self.assertEqual(actual_output, expected_output)

    def test_변수_사용하기(self):
        """ 변수
        파이썬에서 변수는 어떤 것이 들어가도 될 정도로 자유롭습니다.
        함수가 들어가도 되고, 문자열, 정수, 실수 등등 여러가지가 들어갈 수 있습니다.
        굉장히 자유도가 높은 언어인 만큼 *자료형*의 선언이 필요하지 않습니다.
        파이썬에서의 문자열은 ""로 감싸져있습니다. 따라서 10 과 "10"은 다른 형태입니다.
        선언 방법은 등호를 기준으로 왼쪽이 변수명, 오른쪽이 변수입니다.
        """
        number = "10"
        # TODO: number 변수에 정수형 10을 넣어주세요.
        self.assertEqual(number, 10)

    def test_input_입력받기(self):
        """ input()
        파이썬에서의 input()은 사용자의 입력을 받을 수 있습니다.
        input()은 기본적으로 문자열을 저장합니다.
        """
        expected_input = "Alice"
        sys.stdin = StringIO(expected_input)

        try:
            # TODO: input()을 사용하여 사용자로부터 이름을 입력받고, 변수에 저장하세요.
            name = None  # 여기를 수정하세요
        finally:
            sys.stdin = sys.__stdin__

        self.assertEqual(name, expected_input)

    def test_사칙연산_더하기(self):
        """ ➕ 두 숫자를 더하는 연산 """
        a, b = 7, 3
        # TODO: a와 b를 더한 값을 result 변수에 저장하세요.
        result = None  # 여기를 수정하세요
        self.assertEqual(result, 10)

    def test_사칙연산_빼기(self):
        """ ➖ 두 숫자를 빼는 연산 """
        a, b = 10, 4
        # TODO: a에서 b를 뺀 값을 result 변수에 저장하세요.
        result = None  # 여기를 수정하세요
        self.assertEqual(result, 6)

    def test_사칙연산_곱하기(self):
        """ ✖️ 두 숫자를 곱하는 연산 """
        a, b = 5, 5
        # TODO: a와 b를 곱한 값을 result 변수에 저장하세요.
        result = None  # 여기를 수정하세요
        self.assertEqual(result, 25)

    def test_사칙연산_나누기(self):
        """ ➗ 두 숫자를 나누는 연산 """
        a, b = 8, 2
        # TODO: a를 b로 나눈 값을 result 변수에 저장하세요.
        result = None  # 여기를 수정하세요
        self.assertEqual(result, 4)

    def test_사칙연산_나누기_심화(self):
        """ ➗ 두 숫자를 나누고 남은 나머지를 연산 """
        a, b = 17, 6
        # TODO: a를 b로 나눈 후의 나머지 값을 result 변수에 저장하세요.
        result = None  # 여기를 수정하세요
        self.assertEqual(result, 5)

if __name__ == "__main__":
    unittest.main()
