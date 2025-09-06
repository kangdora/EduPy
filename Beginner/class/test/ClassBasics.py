import unittest


class ClassBasicsTest(unittest.TestCase):
    """
    📝 클래스(Class) 기본 개념 테스트

    클래스를 단계적으로 학습하기 위해 아래 순서대로 실습을 진행합니다.

    1️⃣ 클래스 안에서 생성자 정의하기
    2️⃣ 클래스 안에서 메서드 만들기
    3️⃣ 클래스 안에서 인스턴스 변수를 이용한 메서드 만들기
    4️⃣ 클래스 안에서 생성자에 초기화하는 메서드 만들기
    5️⃣ Getter 만들기

    ✅ def 키워드란?
    - Python에서 `def`는 함수를 정의하는 키워드입니다.
    - 클래스 내부에서 `def`를 사용하여 메서드를 정의할 수 있습니다.
    - 메서드는 특정 동작을 수행하며, `self`를 첫 번째 인자로 받아야 합니다.

    ✅ 함수와 메서드의 차이
    - 함수(Function): 독립적으로 정의된 코드 블록 (ex: `def my_function():`)
    - 메서드(Method): 클래스 내부에서 정의된 함수로, 특정 객체와 연관됨 (ex: `def my_method(self):`)

    ✅ 매개변수와 로컬 변수
    - **매개변수(Parameter)**: 함수 또는 메서드를 호출할 때 입력값을 전달받는 변수 (ex: `def add(a, b):`)
    - **로컬 변수(Local Variable)**: 함수 내부에서만 사용되는 변수 (ex: 함수 실행이 끝나면 삭제됨)

    ✅ self란?
    - `self`는 클래스 내부의 메서드에서 해당 객체 자체를 가리키는 키워드입니다.
    - `self`를 사용하여 객체의 속성에 접근하고 수정할 수 있습니다.
    """

    def test_constructor(self):
        """🏗️ 1️⃣ 생성자 정의하기
        생성자는 객체가 처음 생성될 때 실행되는 특별한 메서드입니다.
        하지만 '초기화'란 모든 값을 리셋하는 것이 아니라,
        객체가 가질 기본 상태를 설정하는 과정입니다.
        즉, 객체가 생성될 때 어떤 값으로 시작할지를 정의하는 역할을 합니다.
        """

        class Person:
            # TODO: 생성자를 정의하여 name과 age를 초기화하세요
            pass  # pass 키워드는 무시하셔도 됩니다!

        person = Person("Alice", 25)

        self.assertEqual(person.name, "Alice")
        self.assertEqual(person.age, 25)

    def test_method(self):
        """🏗️ 2️⃣ 메서드 만들기
        클래스 내부에서 동작을 정의하는 함수입니다.
        """

        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age

            # TODO: introduce 메서드를 추가하여 자기소개 문장을 반환하도록 하세요.
            pass

        person = Person("Bob", 30)

        self.assertEqual(person.introduce(), "안녕하세요, 저는 Bob입니다.")

    def test_instance_variable_method(self):
        """🏗️ 3️⃣ 인스턴스 변수를 활용한 메서드 만들기
        인스턴스 변수는 객체마다 개별적으로 저장되는 속성입니다.
        """

        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age

            # TODO: is_adult 메서드를 추가하여 18세 이상이면 True, 아니면 False를 반환하도록 하세요.
            pass

        person1 = Person("Charlie", 20)
        person2 = Person("Dana", 15)

        self.assertTrue(person1.is_adult())
        self.assertFalse(person2.is_adult())

    def test_constructor_initializing_method(self):
        """🏗️ 4️⃣ 생성자에서 초기화하는 메서드 만들기
        생성자에서 특정 메서드를 실행하여 객체가 초기 상태를 설정하도록 만들 수 있습니다.
        생성자가 실행될 때 자동으로 특정 동작을 수행하게 하려면,
        생성자 내부에서 해당 메서드를 호출하면 됩니다.
        """

        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age
                # TODO: five_years_later 메서드를 __init__ 에 추가하여 초기화 될 때, 메서드를 실행시키세요.

            def five_years_later(self):
                self.age += 5

        person = Person("Eve", 40)

        self.assertEqual(person.age, 45)  # 이렇게 객체의 인스턴스 변수에 직접적으로 접근이 가능합니다!

    def test_getter(self):
        """🏗️ 5️⃣ Getter 만들기
        Getter 메서드는 클래스 내부의 속성을 외부에서 접근할 수 있도록 합니다.
        Getter는 클래스 내의 특정 인스턴스 변수를 반환하는 역할을 하며,
        객체의 내부 속성을 직접 수정하지 않고 값을 읽어올 수 있도록 합니다.
        일반적으로 `get_` 접두사를 사용하여 속성을 가져오는 용도로 활용됩니다.
        """

        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age

            # TODO: get_name 메서드를 추가하여 name 값을 반환하도록 하세요.
            pass

        person = Person("Frank", 50)

        self.assertEqual(person.get_name(), "Frank")
