import unittest


class DirectedGraphTest(unittest.TestCase):
    """ 📝 유향 그래프 기본 개념 실습 """

    def test_directed_graph(self):
        graph = {"A": [], "B": []}
        graph["A"].append("B")
        self.assertEqual(graph, {"A": ["B"], "B": []})


if __name__ == '__main__':
    unittest.main()
