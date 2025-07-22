import unittest


class UndirectedGraphTest(unittest.TestCase):
    """ 📝 무향 그래프 기본 개념 실습
    
    무향 그래프는 간선에 방향이 없어 양쪽 정점이 서로 연결됩니다.
    """

    def test_undirected_graph(self):
        """ 🔄 무향 그래프 만들기 """
        graph = {"A": [], "B": []}
        # TODO: A와 B가 서로 연결되도록 간선을 추가하세요.
        self.assertEqual(graph, {"A": ["B"], "B": ["A"]})


if __name__ == '__main__':
    unittest.main()
