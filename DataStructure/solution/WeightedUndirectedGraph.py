import unittest


class WeightedUndirectedGraphTest(unittest.TestCase):
    """ 📝 무향 가중치 그래프 기본 개념 실습 """

    def test_weighted_graph(self):
        graph = {"A": {}, "B": {}}
        graph["A"]["B"] = 3
        graph["B"]["A"] = 3
        self.assertEqual(graph, {"A": {"B": 3}, "B": {"A": 3}})


if __name__ == '__main__':
    unittest.main()
