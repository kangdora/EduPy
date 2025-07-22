import unittest


class DirectedGraphTest(unittest.TestCase):
    """ 📝 유향 그래프 기본 개념 실습
    
    유향 그래프의 간선은 방향을 가지며 한 쪽에서 다른 쪽으로만 이동할 수 있습니다.
    """

    def test_directed_graph(self):
        """ 🔁 유향 그래프 만들기 """
        graph = {"A": [], "B": []}
        # TODO: A에서 B로 향하는 간선을 추가하세요.
        self.assertEqual(graph, {"A": ["B"], "B": []})


if __name__ == '__main__':
    unittest.main()
