from function import calculate
import pytest

@pytest.mark.code
def test_espresso_1_y():
    input1 = "espresso"
    input2 = 1
    input3 = "y"
    expected_result = 50
    actual_result = calculate(input1,input2,input3)
    assert expected_result == actual_result

@pytest.mark.code
def test_cappuccino_1_y():
    input1 = "cappuccino"
    input2 = 1
    input3 = "y"
    expected_result = 55
    actual_result = calculate(input1,input2,input3)
    assert expected_result == actual_result

@pytest.mark.code
def test_late_1_y():
    input1 = "late"
    input2 = 1
    input3 = "y"
    expected_result = 60
    actual_result = calculate(input1,input2,input3)
    assert expected_result == actual_result

@pytest.mark.code
def test_mocha_1_y():
    input1 = "mocha"
    input2 = 1
    input3 = "y"
    expected_result = 65
    actual_result = calculate(input1,input2,input3)
    assert expected_result == actual_result

@pytest.mark.code
def test_espresso_1_n():
    input1 = "espresso"
    input2 = 1
    input3 = "n"
    expected_result = 55
    actual_result = calculate(input1,input2,input3)
    assert expected_result == actual_result

@pytest.mark.code
def test_cappuccino_1_n():
    input1 = "cappuccino"
    input2 = 1
    input3 = "n"
    expected_result = 60
    actual_result = calculate(input1,input2,input3)
    assert expected_result == actual_result

@pytest.mark.code
def test_late_1_n():
    input1 = "late"
    input2 = 1
    input3 = "n"
    expected_result = 65
    actual_result = calculate(input1,input2,input3)
    assert expected_result == actual_result

@pytest.mark.code
def test_mocha_1_n():
    input1 = "mocha"
    input2 = 1
    input3 = "n"
    expected_result = 70
    actual_result = calculate(input1,input2,input3)
    assert expected_result == actual_result

#invalide_input
@pytest.mark.code
def test_amount_invalide_0():
    input1 = "mocha"
    input2 = 0
    input3 = "y"
    expected_result = "order is wrong"
    actual_result = calculate(input1,input2,input3)
    assert expected_result == actual_result

# @pytest.mark.code
def test_glass_invalide():
    input1 = "mocha"
    input2 = 1
    input3 = "p"
    expected_result = "order is wrong"
    actual_result = calculate(input1,input2,input3)
    assert expected_result == actual_result

@pytest.mark.code
def test_amount_invalide_0_5():
    input1 = "mocha"
    input2 = 0.5
    input3 = "y"
    expected_result = "order is wrong"
    actual_result = calculate(input1,input2,input3)
    assert expected_result == actual_result

@pytest.mark.code
def test_amount_invalide_0():
    input1 = "mocha"
    input2 = -1
    input3 = "y"
    expected_result = "order is wrong"
    actual_result = calculate(input1,input2,input3)
    assert expected_result == actual_result

@pytest.mark.code
def test_order_invalide_0():
    input1 = "ggg"
    input2 = 1
    input3 = "y"
    expected_result = "order is wrong"
    actual_result = calculate(input1,input2,input3)
    assert expected_result == actual_result