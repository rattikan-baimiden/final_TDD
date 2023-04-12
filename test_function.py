from function import calculate
import pytest

@pytest.mark.code
def test_espresso_1_y():
    order = "espresso"
    amount = 1
    glass = "y"
    expected_result = 50
    actual_result = calculate(order,amount,glass)
    assert expected_result == actual_result

@pytest.mark.code
def test_cappuccino_1_y():
    order = "cappuccino"
    amount = 1
    glass = "y"
    expected_result = 55
    actual_result = calculate(order,amount,glass)
    assert expected_result == actual_result

@pytest.mark.code
def test_late_1_y():
    order = "late"
    amount = 1
    glass = "y"
    expected_result = 60
    actual_result = calculate(order,amount,glass)
    assert expected_result == actual_result

@pytest.mark.code
def test_mocha_1_y():
    order = "mocha"
    amount = 1
    glass = "y"
    expected_result = 65
    actual_result = calculate(order,amount,glass)
    assert expected_result == actual_result

@pytest.mark.code
def test_espresso_1_n():
    order = "espresso"
    amount = 1
    glass = "n"
    expected_result = 55
    actual_result = calculate(order,amount,glass)
    assert expected_result == actual_result

@pytest.mark.code
def test_cappuccino_1_n():
    order = "cappuccino"
    amount = 1
    glass = "n"
    expected_result = 60
    actual_result = calculate(order,amount,glass)
    assert expected_result == actual_result

@pytest.mark.code
def test_late_1_n():
    order = "late"
    amount = 1
    glass = "n"
    expected_result = 65
    actual_result = calculate(order,amount,glass)
    assert expected_result == actual_result

@pytest.mark.code
def test_mocha_1_n():
    order = "mocha"
    amount = 1
    glass = "n"
    expected_result = 70
    actual_result = calculate(order,amount,glass)
    assert expected_result == actual_result

#amount_invalide
@pytest.mark.code
def test_amount_invalide_0():
    order = "mocha"
    amount = 0
    glass = "y"
    expected_result = "Please input amount integer"
    actual_result = calculate(order,amount,glass)
    assert expected_result == actual_result

@pytest.mark.code
def test_amount_invalide_0_5():
    order = "mocha"
    amount = 0.5
    glass = "y"
    expected_result = "Please input amount integer"
    actual_result = calculate(order,amount,glass)
    assert expected_result == actual_result

@pytest.mark.code
def test_amount_invalide_minus_1():
    order = "mocha"
    amount = -1
    glass = "y"
    expected_result = "Please input amount integer"
    actual_result = calculate(order,amount,glass)
    assert expected_result == actual_result

@pytest.mark.code
def test_amount_invalide_a():
    order = "mocha"
    amount = "a"
    glass = "y"
    expected_result = "Please input amount integer"
    actual_result = calculate(order,amount,glass)
    assert expected_result == actual_result

@pytest.mark.code
def test_amount_invalide_sharp():
    order = "mocha"
    amount = "#"
    glass = "y"
    expected_result = "Please input amount integer"
    actual_result = calculate(order,amount,glass)
    assert expected_result == actual_result

#order_invalid
@pytest.mark.code
def test_order_invalide_str():
    order = "ggg"
    amount = 1
    glass = "y"
    expected_result = "Please input order espresso, cappuccino, late, mocha"
    actual_result = calculate(order,amount,glass)
    assert expected_result == actual_result

@pytest.mark.code
def test_order_invalide_1():
    order = 1
    amount = 1
    glass = "y"
    expected_result = "Please input order espresso, cappuccino, late, mocha"
    actual_result = calculate(order,amount,glass)
    assert expected_result == actual_result

@pytest.mark.code
def test_order_invalide_sharp():
    order = "#"
    amount = 1
    glass = "y"
    expected_result = "Please input order espresso, cappuccino, late, mocha"
    actual_result = calculate(order,amount,glass)
    assert expected_result == actual_result

#glass_invalid
@pytest.mark.code
def test_glass_invalide_str():
    order = "mocha"
    amount = 1
    glass = "p"
    expected_result = "Please input glass y/n"
    actual_result = calculate(order,amount,glass)
    assert expected_result == actual_result

@pytest.mark.code
def test_glass_invalide_int():
    order = "mocha"
    amount = 1
    glass = 1
    expected_result = "Please input glass y/n"
    actual_result = calculate(order,amount,glass)
    assert expected_result == actual_result

@pytest.mark.code
def test_glass_invalide_sharp():
    order = "mocha"
    amount = 1
    glass = "#"
    expected_result = "Please input glass y/n"
    actual_result = calculate(order,amount,glass)
    assert expected_result == actual_result
