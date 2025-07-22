import unittest


class BinaryTreeTest(unittest.TestCase):
    """ 📝 이진 트리 기본 개념 실습
    
    이진 트리는 각 노드가 최대 두 개의 자식을 가지는 트리 구조입니다.
    왼쪽 자식은 작은 값을, 오른쪽 자식은 큰 값을 저장하는 것이 일반적인 규칙입니다.
    """

    def test_binary_tree(self):
        """ 🌳 이진 트리 구성하기 """
        class TreeNode:
            def __init__(self, value):
                self.value = value
                self.left = None
                self.right = None

        root = TreeNode(1)
        left = TreeNode(2)
        right = TreeNode(3)
        # TODO: root의 왼쪽에 left, 오른쪽에 right 노드를 연결하세요.
        self.assertEqual(root.left.value, 2)
        self.assertEqual(root.right.value, 3)


if __name__ == '__main__':
    unittest.main()
