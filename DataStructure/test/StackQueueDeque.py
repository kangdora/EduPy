import unittest
from collections import deque


class StackQueueDequeTest(unittest.TestCase):
    """ 📝 스택, 큐, 덱 기본 개념 실습
    
    스택은 LIFO(Last-In First-Out) 구조로 가장 나중에 들어간 데이터가 가장 먼저
    나옵니다. 큐는 FIFO(First-In First-Out) 구조로 먼저 들어간 데이터가 먼저 나옵
    니다. 덱(deque)은 양쪽에서 삽입과 삭제가 모두 가능한 자료구조입니다.
    """

    def test_stack(self):
        """ 📚 스택 사용하기 """
        stack = []
        # TODO: stack에 1, 2, 3을 차례로 push한 뒤 가장 위의 값을 pop하여 top 변수에 저장하세요.
        top = None  # 여기를 수정하세요
        self.assertEqual(top, 3)
        self.assertEqual(stack, [1, 2])

    def test_queue(self):
        """ 🚶 큐 사용하기 """
        queue = []
        # TODO: queue에 1, 2, 3을 차례로 enqueue한 뒤 가장 앞의 값을 dequeue하여 first 변수에 저장하세요.
        first = None  # 여기를 수정하세요
        self.assertEqual(first, 1)
        self.assertEqual(queue, [2, 3])

    def test_deque(self):
        """ ↔️ 데크 사용하기 """
        dq = deque()
        # TODO: dq의 오른쪽에 1, 2를 추가하고 왼쪽에 0을 추가한 뒤 왼쪽에서 값을 꺼내 left_item 변수에 저장하세요.
        left_item = None  # 여기를 수정하세요
        self.assertEqual(left_item, 0)
        self.assertEqual(list(dq), [1, 2])


if __name__ == '__main__':
    unittest.main()
