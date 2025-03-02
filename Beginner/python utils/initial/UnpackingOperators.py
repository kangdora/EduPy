import unittest


class UnpackingOperators(unittest.TestCase):
    """
    📝 언패킹 연산자 (`*args`, `**kwargs`) 학습

    언패킹 연산자는 Python에서 함수에 여러 개의 인자를 동적으로 전달할 때 사용됩니다.
    `*`는 튜플이나 리스트의 요소를 개별 인자로 전달하고,
    `**`는 딕셔너리의 키-값 쌍을 개별 인자로 전달하는 역할을 합니다.

    ✅ `*args`: 여러 개의 위치 인자를 받을 때 사용
    ✅ `**kwargs`: 여러 개의 키워드 인자를 받을 때 사용
    """

    def test_args_chain_lists(self):
        """
        🏗️ `*args`를 활용한 리스트 병합
        여러 개의 리스트를 하나의 리스트로 병합할 때 사용할 수 있습니다.
        """

        def chain_lists(*args):
            # TODO: 주어진 여러 개의 리스트를 하나의 리스트로 병합하세요.
            return None

        self.assertEqual(chain_lists([1, 2], [3, 4], [5, 6]), [1, 2, 3, 4, 5, 6])

    def test_args_sum_all_elements(self):
        """
        🏗️ `*args`를 활용한 숫자 리스트 합산
        여러 개의 숫자 리스트를 받아 개별 숫자로 처리할 때 사용할 수 있습니다.
        """

        def sum_all_elements(*args):
            # TODO: 주어진 여러 개의 리스트의 모든 요소를 합산하세요.
            return None

        self.assertEqual(sum_all_elements([1, 2], [3, 4], [5, 6]), 21)

    def test_kwargs_merge_dicts(self):
        """
        🏗️ `**kwargs`를 활용한 딕셔너리 병합
        여러 개의 키워드 인자를 받아 하나의 딕셔너리로 병합할 때 사용할 수 있습니다.
        """

        def merge_dicts(**kwargs):
            # TODO: `kwargs`를 활용하여 모든 키-값 쌍을 포함한 하나의 딕셔너리를 반환하세요.
            return None

        self.assertEqual(merge_dicts(a=1, b=2, c=3), {"a": 1, "b": 2, "c": 3})

    def test_args_kwargs_format_strings(self):
        """
        🏗️ `*args`와 `**kwargs`를 활용한 문자열 포맷팅
        여러 개의 문자열을 다양한 방식으로 포맷팅할 때 사용할 수 있습니다.
        """

        def format_strings(format_type, *args, **kwargs):
            # TODO: 주어진 문자열을 format_type에 맞게 변환하세요.
            return None

        self.assertEqual(format_strings("csv", "Alice", "Bob", "Charlie"), "Alice,Bob,Charlie")
        self.assertEqual(format_strings("json", name="Alice", age=25), '{"name": "Alice", "age": 25}')

    def test_args_kwargs_combined(self):
        """
        🏗️ `*args`와 `**kwargs`를 동시에 활용한 복합적인 함수
        위치 인자와 키워드 인자를 함께 받아 가변적인 데이터 처리가 가능하도록 합니다.
        """

        def process_data(*args, **kwargs):
            # TODO: `*args`를 리스트로 병합하고, `**kwargs`는 딕셔너리로 반환하세요.
            return None

        self.assertEqual(
            process_data([1, 2], [3, 4], key1="value1", key2="value2"),
            ([1, 2, 3, 4], {"key1": "value1", "key2": "value2"})
        )
