import unittest


class WeightedUndirectedGraphTest(unittest.TestCase):
    """ 📝 무향 가중치 그래프 기본 개념 실습
    
    간선마다 가중치가 있으며 방향이 없는 그래프 구조를 만들어 봅니다.
    """

    def test_weighted_graph(self):
        """ ⚖️ 무향 가중치 그래프 만들기 """
        graph = {"A": {}, "B": {}}
        # TODO: A와 B 사이에 가중치 3의 간선을 양방향으로 추가하세요.
        self.assertEqual(graph, {"A": {"B": 3}, "B": {"A": 3}})


if __name__ == '__main__':
    unittest.main()
