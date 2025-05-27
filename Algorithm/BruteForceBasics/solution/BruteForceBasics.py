import random
import sys
import unittest
from io import StringIO


class BruteForceBasics(unittest.TestCase):
    """ 🔍 브루트포스 알고리즘 기초 단원
    브루트포스 알고리즘은 가능한 모든 경우의 수를 하나씩 전부 시도해보는 방식입니다.
    정답이 보장된 경우, 가장 직관적인 접근법이기 때문에 초심자에게 적합합니다.

    이 단원에서는 브루트포스의 핵심인 "모든 조합을 직접 시도해보기" 를 간단한 숫자 예제로 연습합니다.
    for문을 중첩하여 모든 경우를 나열하는 방법, 그 결과를 리스트에 저장하는 방법 등을 배우게 됩니다.

    이러한 연습을 통해, 복잡한 문제에서도 어떻게 "가능한 모든 경우"를 구성하고,
    그 안에서 조건을 비교하며 정답을 찾아낼 수 있는지를 체험하게 됩니다.

    이 과정을 거치면, 여러분은 실버 브루트포스 문제에 도전할 수 있는 기본기를 갖추게 됩니다.
    """

    def setUp(self):
        self._stdout_backup = sys.stdout
        self.stdout = StringIO()
        sys.stdout = self.stdout

    def tearDown(self):
        sys.stdout = self._stdout_backup

    def test_모든_두_숫자_조합의_합(self):
        """ ➕ 0~9까지 두 숫자의 모든 합 구하기 """
        rand = random.randint(1, 99)
        results = []
        for a in range(10):
            for b in range(10):
                results.append(a + b)

        print(results[rand])

        self.assertEqual(len(results), 100)
        self.assertEqual(int(self.stdout.getvalue().strip()), results[rand])

    def test_세_개의_숫자_모든_조합의_곱(self):
        """ ✖️ 1~3까지 세 숫자를 골라 곱한 결과 모두 구하기 """
        results = []
        for a in range(1, 4):
            for b in range(1, 4):
                for c in range(1, 4):
                    results.append(a * b * c)

        print(*results)

        self.assertIn(27, results)
        self.assertEqual(self.stdout.getvalue().strip(), " ".join(map(str, results)))

    def test_암호_맞추기(self):
        """ 🔐 정답이 랜덤일 때, 0~99 모든 숫자를 대입해 어떤 숫자가 정답인지 확인 """
        secret = random.randint(1, 100)
        found = False

        for guess in range(100):
            if guess == secret:
                found = True
                print(guess)
                break

        self.assertTrue(found)
        self.assertEqual(int(self.stdout.getvalue().strip()), secret)
