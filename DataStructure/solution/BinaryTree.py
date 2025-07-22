import unittest


class BinaryTreeTest(unittest.TestCase):
    """ 📝 이진 트리 기본 개념 실습 """

    def test_binary_tree(self):
        class TreeNode:
            def __init__(self, value):
                self.value = value
                self.left = None
                self.right = None

        root = TreeNode(1)
        left = TreeNode(2)
        right = TreeNode(3)
        root.left = left
        root.right = right
        self.assertEqual(root.left.value, 2)
        self.assertEqual(root.right.value, 3)


if __name__ == '__main__':
    unittest.main()
