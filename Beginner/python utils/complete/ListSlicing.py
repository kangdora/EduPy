import unittest
import copy


class ListSlicingTest(unittest.TestCase):
    """📝 리스트 슬라이싱 (List Slicing) 학습

    리스트 슬라이싱은 리스트의 특정 부분을 선택하여 추출하는 강력한 기능입니다.

    ✅ 기본 구조:
    리스트[start:end:step]
    - start: 시작 인덱스 (생략하면 처음부터)
    - end: 끝 인덱스 (해당 인덱스 이전까지 포함)
    - step: 증가 간격 (생략하면 1씩 증가)

    ✅ 활용 예시:
    numbers = [0, 1, 2, 3, 4, 5]
    print(numbers[1:4])  # [1, 2, 3]
    print(numbers[:3])   # [0, 1, 2] (처음부터 3번째 전까지)
    print(numbers[2:])   # [2, 3, 4, 5] (2번 인덱스부터 끝까지)
    print(numbers[::-1]) # [5, 4, 3, 2, 1, 0] (역순 정렬)

    ✅ 깊은 복사 vs 얕은 복사
    - 얕은 복사 (Shallow Copy): 새로운 객체를 생성하지만 내부 요소는 원본과 공유됨.
    - 깊은 복사 (Deep Copy): 새로운 객체뿐만 아니라 내부 요소까지 새로운 객체로 복사됨.

    shallow_copy = original_list[:]
    deep_copy = copy.deepcopy(original_list)
    """

    def test_slice_from_start(self):
        """🏗️ 특정 인덱스부터 끝까지 슬라이싱"""

        numbers = [0, 1, 2, 3, 4, 5]

        sliced = numbers[2:]

        self.assertEqual(sliced, [2, 3, 4, 5])

    def test_slice_until_end(self):
        """🏗️ 처음부터 특정 인덱스 전까지 슬라이싱"""

        numbers = [0, 1, 2, 3, 4, 5]

        sliced = numbers[:3]

        self.assertEqual(sliced, [0, 1, 2])

    def test_slice_full_copy(self):
        """🏗️ `[:]`을 이용한 전체 리스트 복사 (얕은 복사)"""

        numbers = [0, 1, 2, 3, 4, 5]

        copied = numbers[:]

        self.assertEqual(copied, numbers)
        self.assertIsNot(copied, numbers)  # 서로 다른 객체여야 함

    def test_slice_reverse(self):
        """🏗️ `[::-1]`을 이용한 리스트 역순 정렬"""

        numbers = [0, 1, 2, 3, 4, 5]

        reversed_list = numbers[::-1]

        self.assertEqual(reversed_list, [5, 4, 3, 2, 1, 0])

    def test_deep_copy_vs_shallow_copy(self):
        """🏗️ 깊은 복사 vs 얕은 복사
        `[:]`을 이용한 얕은 복사와 `copy.deepcopy()`를 이용한 깊은 복사를 비교합니다.
        """

        original = [[1, 2, 3], [4, 5, 6]]
        shallow_copied = original[:]  # 얕은 복사
        deep_copied = copy.deepcopy(original)  # 깊은 복사

        original[0][0] = 0  # 가변 객체 내부 값 변경

        self.assertEqual(original, shallow_copied)  # ✅ shallow_copied도 영향 받음 → 통과
        self.assertNotEqual(original, deep_copied)  # ✅ deep_copied는 영향 없음 → 통과
