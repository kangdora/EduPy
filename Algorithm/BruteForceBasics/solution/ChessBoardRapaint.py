import sys
import unittest
from io import StringIO


class ChessBoardRepaint(unittest.TestCase):
    """ ♟️ 체스판 다시 칠하기 단원
    이 단원에서는 복잡한 하나의 문제를 단계적으로 분해해가며 해결하는 과정을 학습합니다.
    목표는 백준 1018번 문제를 완전히 해결할 수 있는 실력을 기르는 것이며,
    이를 위해 입력 처리, 패턴 비교, 부분 탐색, 통합 등의 과정을 차례대로 연습합니다.
    """

    def setUp(self):
        self._stdout_backup = sys.stdout
        self.stdout = StringIO()
        sys.stdout = self.stdout

    def tearDown(self):
        sys.stdout = self._stdout_backup

    def test_입력파싱(self):
        """ 📥 문자열 리스트를 2차원 리스트 형태로 변환하기 """
        raw = [
            "WBWBWBWB",
            "BWBWBWBW"
        ]

        board = [list(row) for row in raw]

        self.assertEqual(board, [['W','B','W','B','W','B','W','B'], ['B','W','B','W','B','W','B','W']])

    def test_2x2_순회_4x4(self):
        """ 🧭 4x4 보드에서 2x2 모든 영역 탐색 연습 """
        board = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]

        sub_sums = []
        for i in range(len(board) - 1):
            for j in range(len(board[0]) - 1):
                sub_sums.append(board[i][j] + board[i][j + 1] + board[i + 1][j] + board[i + 1][j + 1])

        self.assertEqual(len(sub_sums), 9)
        self.assertIn(14, sub_sums)  # 예: 1+2+5+6
        self.assertIn(54, sub_sums)  # 예: 11+12+15+16

    def test_패턴비교_함수(self):
        """ 🎨 8x8 보드와 체스 패턴 비교하여 다시 칠할 칸 수 구하기 """
        # 체스보드판처럼, 백이 W, 흑이 B라고 가정하고, 한개의 보드에서는 흑백이 번갈아가며 나와야 합니다.
        board = [
            list("BWBWBWBW"),
            list("WBWBWBWB"),
            list("BWBWBWBW"),
            list("WBWBWBWB"),
            list("BWBWBWBW"),
            list("WBWBWBWB"),
            list("BWBWBWBW"),
            list("WBBBBBBB")
        ]

        repaint_w = 0  # 처음 문자가 W일때, 다시 칠해야 하는 개수
        repaint_b = 0  # 처음 문자가 B일때, 다시 칠해야 하는 개수

        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    if board[i][j] == "W":
                        repaint_b += 1
                    else:
                        repaint_w += 1
                else:
                    if board[i][j] == "W":
                        repaint_w += 1
                    else:
                        repaint_b += 1

        # 조금 더 머리를 사용하면, repaint_w = 64 - repaint_b 입니다.

        ########################################################################################
        ## HINT: 1, 1이 B라고 가정할 때, 1, 2는 W입니다. 이 좌표의 합은 짝수와 홀수라고 정의할 수 있습니다.
        ########################################################################################

        print(min(repaint_w, repaint_b))

        self.assertEqual(repaint_w, 61)
        self.assertEqual(repaint_b, 3)
        self.assertEqual(int(self.stdout.getvalue().strip()), 3)

    def test_전체보드에서_최소값_탐색(self):
        """ 🔍 전체 보드에서 8x8 구간을 완전탐색하여 최소 칠하기 수 찾기 """
        board = [
            list("BBBBBBBBWBWBW"),
            list("BBBBBBBBBWBWB"),
            list("BBBBBBBBWBWBW"),
            list("BBBBBBBBBWBWB"),
            list("BBBBBBBBWBWBW"),
            list("BBBBBBBBBWBWB"),
            list("BBBBBBBBWBWBW"),
            list("BBBBBBBBBWBWB"),
            list("WWWWWWWWWWBWB"),
            list("WWWWWWWWWWBWB")
        ]

        def search(x, y):
            result = 0
            for i in range(8):
                for j in range(8):
                    if (i + j) % 2 == 0:
                        if board[y + j][x + i] == "W":
                            result += 1
                    else:
                        if board[y + j][x + i] == "B":
                            result += 1
            return min(result, 64 - result)

        ans = 64

        for y in range(len(board) - 7):
            for x in range(len(board[0]) - 7):
                ans = min(search(x, y), ans)

        print(ans)

        self.assertEqual(int(self.stdout.getvalue().strip()), 12)