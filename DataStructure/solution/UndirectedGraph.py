import unittest


class UndirectedGraphTest(unittest.TestCase):
    """ 📝 무향 그래프 기본 개념 실습 """

    def test_undirected_graph(self):
        graph = {"A": [], "B": []}
        graph["A"].append("B")
        graph["B"].append("A")
        self.assertEqual(graph, {"A": ["B"], "B": ["A"]})


if __name__ == '__main__':
    unittest.main()
