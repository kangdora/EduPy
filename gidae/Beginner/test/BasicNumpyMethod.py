import unittest
import numpy as np


class BasicNumpyMethod(unittest.TestCase):
    """📝 기초데이터 다룰때 사용하는 NumPy에 대한 개념 실습

    Python의 기본 자료형인 ``list``는 다양한 자료형을 혼합하여 담을 수 있는 반면,
    NumPy의 ``ndarray``는 **하나의 자료형(dtype)** 만을 저장하는 고정형 배열입니다.
    이러한 특성 덕분에 NumPy는 대규모 수치 계산에서 빠르고 효율적인 연산을
    제공합니다.

    이 단원에서는 ``list`` 와 ``ndarray`` 의 차이를 살펴보고, ``zeros`` 와 ``ones``
    같은 생성 메서드, ``reshape`` 를 이용한 구조 변환, 그리고 ``axis`` 를 지정한
    집계 연산을 통해 **정수형** 과 **실수형** 자료를 다루는 방법을 연습합니다.
    """

    def test_list_vs_ndarray(self):
        """ 📚 ``list`` 와 ``ndarray`` 의 자료형 비교 """
        py_list = [1, 2, 3]
        np_array = np.array(py_list)

        list_type = type(py_list)
        ndarray_type = type(np_array)

        dtype_kind = None  # TODO: np_array의 dtype kind를 가져오세요.

        self.assertIs(list_type, list)
        self.assertIs(ndarray_type, np.ndarray)
        self.assertEqual(dtype_kind, "i")

    def test_array_with_float(self):
        """ 🌊 실수형 ``ndarray`` 만들기 """
        float_array = np.array([1.0, 2.0, 3.0])

        dtype_kind = None  # TODO: float_array의 dtype kind를 가져오세요.

        self.assertEqual(dtype_kind, "f")

    def test_basic_creation_methods(self):
        """ 🧱 ``zeros`` 와 ``ones`` 기본 메서드 사용하기 """
        zero_int_array = None  # TODO: 길이 3의 정수형 0 배열을 생성하세요.
        one_float_array = None  # TODO: 길이 3의 실수형 1 배열을 생성하세요.

        self.assertEqual(zero_int_array.dtype.kind, "i")
        self.assertEqual(one_float_array.dtype.kind, "f")

    def test_array_reshape(self):
        """ 🔄 ``reshape`` 로 배열 형태 바꾸기 """
        base_array = np.arange(6)

        reshaped = None  # TODO: ``base_array`` 를 (2, 3) 형태로 바꾸세요.

        self.assertEqual(reshaped.shape, (2, 3))
        self.assertEqual(reshaped.dtype.kind, "i")

    def test_axis_operations(self):
        """ 📐 ``axis`` 를 기준으로 합 구하기 """
        matrix = np.array([[1, 2, 3], [4, 5, 6]])

        axis0_sum = None  # TODO: ``axis=0`` 기준으로 합을 구하세요.
        axis1_sum = None  # TODO: ``axis=1`` 기준으로 합을 구하세요.

        self.assertTrue(np.all(axis0_sum == np.array([5, 7, 9])))
        self.assertTrue(np.all(axis1_sum == np.array([6, 15])))
