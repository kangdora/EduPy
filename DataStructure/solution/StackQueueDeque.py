import unittest
from collections import deque


class StackQueueDequeTest(unittest.TestCase):
    """ 📝 스택, 큐, 덱 기본 개념 실습 """

    def test_stack(self):
        stack = []
        stack.append(1)
        stack.append(2)
        stack.append(3)
        top = stack.pop()
        self.assertEqual(top, 3)
        self.assertEqual(stack, [1, 2])

    def test_queue(self):
        queue = []
        queue.append(1)
        queue.append(2)
        queue.append(3)
        first = queue.pop(0)
        self.assertEqual(first, 1)
        self.assertEqual(queue, [2, 3])

    def test_deque(self):
        dq = deque()
        dq.append(1)
        dq.append(2)
        dq.appendleft(0)
        left_item = dq.popleft()
        self.assertEqual(left_item, 0)
        self.assertEqual(list(dq), [1, 2])


if __name__ == '__main__':
    unittest.main()
