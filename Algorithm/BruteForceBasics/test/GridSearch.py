import unittest
import sys
from io import StringIO

class GridSearch(unittest.TestCase):
    """ 🧭 2차원 배열 완전탐색 단원
    이 단원에서는 2차원 리스트에서 부분 영역(서브보드)을 선택하고,
    그 내부 값을 탐색하거나 조건을 적용하는 연습을 합니다.

    브루트포스 알고리즘이 2차원 구조에 적용되는 방식과,
    각 셀을 접근하는 인덱스 구조를 익히는 것이 핵심입니다.
    이후 복잡한 체스판 문제, 패턴 인식 문제 등으로 연결됩니다.
    """

    def setUp(self):
        self._stdout_backup = sys.stdout
        self.stdout = StringIO()
        sys.stdout = self.stdout

    def tearDown(self):
        sys.stdout = self._stdout_backup

    def test_3x3_부분합(self):
        """ 🔲 시작점 (2, 3)에서 3x3 영역의 합 구하기 """
        # 왼쪽 위의 점이 1,1입니다
        board = [
            [1,2,3,4,5,6,7,8],
            [2,3,4,5,6,7,8,1],
            [3,4,5,6,7,8,1,2],
            [4,5,6,7,8,1,2,3],
            [5,6,7,8,1,2,3,4],
            [6,7,8,1,2,3,4,5],
            [7,8,1,2,3,4,5,6],
            [8,1,2,3,4,5,6,7]
        ]
        start_row, start_col = 2, 3
        result = 0
        # TODO: 시작 위치부터 3x3 영역의 값을 모두 더한 결과를 출력하세요.

        self.assertEqual(self.stdout.getvalue().strip(), 54)

    def test_모든_2x2_영역_중_최댓값(self):
        """ 🟨 모든 2x2 부분보드 중 합이 가장 큰 값 구하기 """
        board = [
            [1, 2, 1, 2],
            [3, 4, 3, 4],
            [1, 2, 1, 2],
            [3, 4, 3, 4]
        ]

        max_sum = 0
        # TODO: 모든 2x2 구간을 탐색해, 각 구간의 합 중 최댓값을 출력하세요.

        self.assertEqual(self.stdout.getvalue().strip(), 14)  # (3+4+3+4)

    def test_3x3_안에서_5이상_숫자_갯수(self):
        """ 🔢 시작 위치 (1, 2)에서 3x3 영역 내 5 이상인 숫자의 개수 구하기 """
        # 왼쪽 위의 점이 1,1입니다
        board = [
            [1, 2, 3, 4, 5],
            [5, 6, 7, 8, 9],
            [9, 8, 7, 6, 5],
            [4, 3, 2, 1, 0]
        ]

        start_row, start_col = 1, 2
        count = 0

        # TODO: 3x3 영역 안에서 5 이상인 숫자의 개수를 출럭하세요.

        self.assertEqual(self.stdout.getvalue().strip(), 6)

    def test_문자_패턴_확인(self):
        """ ♟️ 2x2 영역이 모두 'W'로 채워진 경우가 있는지 확인 """
        board = [
            ['B', 'W', 'W'],
            ['W', 'W', 'B'],
            ['B', 'W', 'W']
        ]

        # TODO: 2x2 영역 중 모두 'W'로 채워진 곳이 있다면 1을 출력하고, 없다면 0을 출력하세요.

        self.assertEqual(self.stdout.getvalue().strip(), 0)

