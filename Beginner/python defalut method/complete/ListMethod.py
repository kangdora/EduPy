import unittest


class ListMethod(unittest.TestCase):
    """
    📝 리스트 기본 메서드 테스트

    리스트의 메서드들을 학습하기 위한 단원입니다.

    이 단원부터는 중요도가 들어갑니다.
    ⭐⭐⭐  - 매우 중요
    ⭐⭐✩  - 가끔 사용
    ⭐✰ ✰ - 있다는 것만 알아도 됨

    0️⃣1️⃣ extend ⭐⭐✩
    0️⃣2️⃣ pop ⭐⭐⭐
    0️⃣3️⃣ copy ⭐⭐✩
    0️⃣4️⃣ sort ⭐⭐⭐
    0️⃣5️⃣ count ⭐⭐✩
    0️⃣6️⃣ append ⭐⭐⭐
    0️⃣7️⃣ clear ⭐✰ ✰
    0️⃣8️⃣ index ⭐⭐✩
    0️⃣9️⃣ insert ⭐⭐✩
    1️⃣0️⃣ remove ⭐⭐✰
    1️⃣1️⃣ reverse ⭐✰ ✰

    메서드는 기본적으로 객체.메서드 형태로 사용이 됩니다.
    메서드마다 반환형식이 있는것도 있고, 없는것도 있습니다.
    중요도는 작성자인 저를 기준으로 작성되었습니다.

    """

    def test_list_extend(self):
        """ 🏗️ extend
        list와 다른 객체를 연결해주는 메서드입니다.
        list.extend(다른 객체) 형태로 사용됩니다.
        """

        original_list = [1, 2, 3]
        another_list = [4, 5, 6]

        original_list.extend(another_list)

        self.assertEqual(original_list, [1, 2, 3, 4, 5, 6])

    def test_list_pop(self):
        """ 🏗️ pop
        리스트의 마지막 요소 또는 특정 인덱스의 요소를 제거하고 반환합니다.
        list.pop() 형태로 사용하며, 받아주는 변수는 선택적입니다.
        """

        numbers = [1, 2, 3, 4, 5]

        last_element = numbers.pop()

        self.assertEqual(last_element, 5)
        self.assertEqual(numbers, [1, 2, 3, 4])

    def test_list_copy(self):
        """ 🏗️ copy
        리스트의 얕은 복사를 수행합니다. 얕은 복사란, 새로운 리스트 객체를 생성하지만, 내부 요소(원소)는 기존 리스트와 동일한 참조값(메모리 주소)을 공유하는 방식입니다.
        만약 C의 포인터 개념을 알고 계신다면, Python의 리스트는 내부적으로 각 원소가 메모리 주소를 가리키는 참조형 객체로 저장되므로
        리스트를 복사하면 원소들의 참조값만 복사된다고 이해할 수 있습니다.

        즉, 복사된 리스트에서 원소를 수정하면 원본 리스트도 영향을 받을 수 있습니다.
        하지만 리스트 자체를 변경(예: `.append()`, `.pop()` 등)하면 영향을 받지 않습니다.
        """

        original = [1, 2, 3]

        copied = original.copy()

        self.assertEqual(copied, original)
        self.assertIsNot(copied, original)  # 서로 다른 객체여야 함

    def test_list_sort(self):
        """ 🏗️ sort
        리스트를 정렬하는 메서드입니다.
        파이썬에서 sort는 TimSort를 사용합니다.
        필요하시다면 TimSort에 대해 찾아보시는 것도 추천합니다.
        """

        numbers = [3, 1, 4, 1, 5, 9]

        numbers.sort()

        self.assertEqual(numbers, [1, 1, 3, 4, 5, 9])

    def test_list_count(self):
        """ 🏗️ count
        리스트 내 특정 요소의 개수를 반환합니다.
        """

        numbers = [1, 2, 2, 3, 3, 3, 4]

        count_three = numbers.count(3)

        self.assertEqual(count_three, 3)

    def test_list_append(self):
        """ 🏗️ append
        리스트의 끝에 요소를 추가합니다.
        """

        numbers = [1, 2, 3]

        numbers.append(4)

        self.assertEqual(numbers, [1, 2, 3, 4])

    def test_list_clear(self):
        """ 🏗️ clear
        리스트의 모든 요소를 제거합니다. 기존 객체는 보존됩니다.
        """

        numbers = [1, 2, 3]

        numbers.clear()

        self.assertEqual(numbers, [])

    def test_list_index(self):
        """ 🏗️ index
        리스트에서 특정 요소의 첫 번째 인덱스를 반환합니다.
        만약, [1, 1, 1, 1, 1]의 경우 제일 앞에 있는 0번째 요소인 0을 반환합니다.
        """

        numbers = [10, 20, 30, 40]

        index_of_30 = numbers.index(30)

        self.assertEqual(index_of_30, 2)

    def test_list_insert(self):
        """ 🏗️ insert
        특정 인덱스에 요소를 삽입합니다.
        """

        numbers = [1, 2, 4]

        numbers.insert(2, 3)

        self.assertEqual(numbers, [1, 2, 3, 4])

    def test_list_remove(self):
        """ 🏗️ remove
        리스트에서 첫 번째로 발견된 특정 요소를 제거합니다.
        """

        numbers = [10, 20, 30, 20, 40]

        numbers.remove(20)

        self.assertEqual(numbers, [10, 30, 20, 40])

    def test_list_reverse(self):
        """ 🏗️ reverse
        리스트의 요소 순서를 뒤집습니다.
        reversed_list = list[::-1] 과 비슷한 역할을 합니다.

        list[::-1] 새로운 객체를 생성하여 복사합니다. 하지만 reverse의 경우 새로운 객체를 생성하지 않아 메모리 관리에 효율적입니다.
        """

        numbers = [1, 2, 3, 4]

        numbers.reverse()

        self.assertEqual(numbers, [4, 3, 2, 1])
