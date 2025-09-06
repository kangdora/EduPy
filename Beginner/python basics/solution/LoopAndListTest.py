import unittest


class LoopAndListTest(unittest.TestCase):
    """ 🔄 반복문과 리스트 (초심자용)

    반복문은 특정 동작을 여러 번 실행할 때 사용됩니다.

    1. for 반복문
       리스트나 튜플의 요소를 하나씩 꺼내어 반복할 때 사용합니다.
       문법: for 변수 in 리스트: 실행할 코드
       예제:
         numbers = [1, 2, 3]
         for num in numbers:
             print(num)
       위 코드는 리스트 [1, 2, 3]의 요소를 하나씩 출력합니다.

    2. while 반복문
       특정 조건이 True일 동안 반복 실행됩니다.
       문법: while 조건: 실행할 코드
       예제:
         count = 0
         while count < 3:
             print(count)
             count += 1
       위 코드는 count가 3이 될 때까지 반복 실행됩니다.

    3. 리스트(List)
       여러 개의 값을 저장하는 자료구조입니다.
       예제:
         numbers = [1, 2, 3, 4, 5]
         print(numbers[0])  # 첫 번째 요소 출력
       리스트는 in 연산자로 포함 여부를 확인할 수 있습니다.
    """

    def test_for_반복문(self):
        """ 🔁 `for` 루프를 사용하여 리스트 순회하기 """
        numbers = [1, 2, 3, 4, 5]
        result = []

        for num in numbers:
            result.append(num)

        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_while_반복문(self):
        """ 🔄 `while` 루프를 사용하여 1부터 5까지 리스트에 추가하기 """
        result = []
        num = 1

        # TODO: while문을 사용하여 num이 5 이하일 때까지 result에 추가하세요.
        while num < 6:
            result.append(num)
            num += 1

        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_range_사용(self):
        """ 🔢 `range()`를 활용하여 숫자 리스트 만들기

        range(시작, 끝)을 사용하면 숫자의 범위를 지정할 수 있습니다.

        예제 1: list()를 사용하여 리스트 변환
          list(range(1, 6))  # [1, 2, 3, 4, 5]

        예제 2: 리스트 컴프리헨션을 활용하는 방법
          [i for i in range(1, 6)]  # [1, 2, 3, 4, 5]

        리스트 컴프리헨션은 파이썬의 고유 문법으로 잘 사용하신다면 엄청난 강점으로 작용할 수 있습니다.

        """
        result1 = list(range(1, 6))
        result2 = [i for i in range(1, 6)]

        self.assertEqual(result1, [1, 2, 3, 4, 5])
        self.assertEqual(result2, [1, 2, 3, 4, 5])

    def test_리스트_내_포함여부_확인(self):
        """ 🔎 `in` 연산자를 사용하여 리스트 내 값 확인 """
        fruits = ["apple", "banana", "cherry"]

        result = "banana" in fruits
        self.assertEqual(result, True)

    def test_리스트_원소_합계(self):
        """ ➕ 리스트의 모든 원소 합 구하기
        sum() 함수는 인자로 들어온 수들의 합을 반환합니다.
        sum(1, 2, 3, 4, 5)로도 사용이 가능하지만, sum(range(1,6)) 도 같은 결과를 도출합니다
        """
        numbers = [10, 20, 30, 40, 50]
        result = sum(numbers)
        self.assertEqual(result, 150)


if __name__ == "__main__":
    unittest.main()
