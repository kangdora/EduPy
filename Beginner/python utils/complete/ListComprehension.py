import unittest


class ListComprehension(unittest.TestCase):
    """
    📝 리스트 컴프리헨션 (List Comprehension) 학습

    리스트 컴프리헨션은 기존의 `for` 루프를 한 줄로 간결하게 표현하는 방법입니다.

    ✅ 기본 구조:
    `[표현식 for 요소 in 반복가능한객체 if 조건]`

    ✅ 장점:
    - 코드의 가독성을 높이고, 간결하게 작성 가능 -> 가독성의 경우 상황에 따라 다름
    - 일반적인 `for` 루프보다 빠른 실행 속도를 가질 수 있음
    - 리스트, 튜플, 딕셔너리, 세트 등의 다양한 자료형에서 사용 가능

    ✅ 일반적인 `for` 루프와의 비교:
    ```python
    # 기존 for문 방식
    squares = []
    for i in range(1, 6):
        squares.append(i ** 2)

    # 리스트 컴프리헨션 방식
    squares = [i ** 2 for i in range(1, 6)]
    ```
    위 방식은 동일한 결과를 출력하지만, 리스트 컴프리헨션을 사용하면 더 간결한 코드 작성이 가능합니다.
    """

    def test_basic_list_comprehension(self):
        """🏗️ 기본적인 리스트 컴프리헨션 사용
        기존의 `for` 루프를 한 줄로 변환하여 리스트를 생성합니다.
        """

        squares = [i ** 2 for i in range(1, 6)]

        self.assertEqual(squares, [1, 4, 9, 16, 25])

    def test_list_comprehension_with_condition(self):
        """🏗️ 조건을 포함한 리스트 컴프리헨션
        특정 조건을 만족하는 요소만 포함하도록 필터링할 수 있습니다.

        ✅ 예제: 1부터 10까지의 숫자 중 짝수만 포함하는 리스트 생성
        기존 for문 방식:
        evens = []
        for i in range(1, 11):
            if i % 2 == 0:
                evens.append(i)
        """

        evens = [i for i in range(1, 11) if i % 2 == 0]

        self.assertEqual(evens, [2, 4, 6, 8, 10])

    def test_nested_list_comprehension(self):
        """🏗️ 중첩된 리스트 컴프리헨션
        2차원 리스트를 한 줄로 변환할 때 사용할 수 있습니다.

        ✅ 기존 for문 방식:
        flattened = []
        for row in matrix:
            for item in row:
                flattened.append(item)
        """

        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        flattened = [i for row in matrix for i in row]

        self.assertEqual(flattened, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_dict_comprehension(self):
        """🏗️ 딕셔너리 컴프리헨션
        키-값 쌍을 포함하는 새로운 딕셔너리를 생성할 수 있습니다.

        ✅ 기존 for문 방식:
        my_dict = {}
        for k, v in zip(keys, values):
            my_dict[k] = v
        """

        keys = ['a', 'b', 'c']
        values = [1, 2, 3]

        my_dict = {k: v for k, v in zip(keys, values)}

        self.assertEqual(my_dict, {'a': 1, 'b': 2, 'c': 3})
