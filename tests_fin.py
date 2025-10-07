import pytest
from unittest.mock import patch
import importlib
import sys

#граничные значения для 32битного int
INT_MAX = 2_147_483_647
INT_MIN = -2_147_483_648


#вспомогательная функция для всех тестов
def run_calculator_with_mocked_io(inputs):
    with patch("builtins.input", side_effect=inputs), patch("builtins.print") as mock_print:
        # для случае если модуль уже загружен — перезагружаем, чтобы код выполнился заново
        if "calculator" in sys.modules:
            importlib.reload(sys.modules["calculator"])
        else:
            import calculator
    return mock_print


#тесты


def test_add_operation():
    mock_print = run_calculator_with_mocked_io(["1", "3", "5"])
    mock_print.assert_any_call(3, "+", 5, "=", 8)


def test_subtract_operation():
    mock_print = run_calculator_with_mocked_io(["2", "3", "10"])
    mock_print.assert_any_call(3, "-", 10, "=", -7)


def test_multiply_operation():
    mock_print = run_calculator_with_mocked_io(["3", "7", "6"])
    mock_print.assert_any_call(7, "*", 6, "=", 42)


def test_multiply_int_max():
    mock_print = run_calculator_with_mocked_io(["3", str(INT_MAX), "1"])
    mock_print.assert_any_call(INT_MAX, "*", 1, "=", INT_MAX)


def test_multiply_with_zero():
    mock_print = run_calculator_with_mocked_io(["3", "7", "0"])
    mock_print.assert_any_call(7, "*", 0, "=", 0)


def test_divide_operation():
    mock_print = run_calculator_with_mocked_io(["4", "10", "2"])
    mock_print.assert_any_call(10, "/", 2, "=", 5)
