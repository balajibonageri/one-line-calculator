from one_line_calculator import calculator

def get_expression(string):
    calculator.input = lambda *args: string
    expression = calculator.expression()
    output = calculator.calculate(expression)
    return output

def get_correct_expression(string):
    calculator.input = lambda *args: string
    output = calculator.expression()
    return output

class TestClass(object):
    def test_expression(self):
        """Remove spacing"""
        output = get_correct_expression(' space space ')
        assert output == 'spacespace'

    def test_expression_two(self):
        """Checking for correct expression"""
        output = get_correct_expression(' 1 + 2 ')
        assert output == '1+2'

    def test_calculate_addition(self):
        """Addition correctly"""
        output = get_expression(' 1 + 2 ')
        assert output == 3

    def test_calculate_multiply(self):
        """multiplication correctly"""
        output = get_expression(' 4 * 2')
        assert output == 8

    def test_calculate_multiply_x(self):
        """multiplication with x"""
        expression = calculator.turn_into_list('4x2')
        output = get_expression('4x2')
        assert output == 8

    def test_calculate_multiply_X(self):
        """multiplication with X"""
        output = get_expression('4 X 2')
        assert output == 8

    def test_calculate_division(self):
        """division correctly"""
        output = get_expression('4 / 2')
        assert output == 2

    def test_calculate_power(self):
        """Power with ^"""
        output = get_expression('2^3')
        assert output == 8

    def test_calculate_power_star(self):
        """Power with **"""
        output = get_expression('2**3')
        assert output == 8

    def test_turn_into_list(self):
        """Check for bugs in function"""
        expression = get_correct_expression(' 2 * * 4 + 3')
        output = calculator.turn_into_list(expression)
        assert output == ['2', '^', '4', '+', '3']

    def test_calculate_pEMDAS(self):
        # 8+8-2*32/2**3
        # 8+8-2*32/8
        # 8+8-64/8
        # 8+8-8
        # 16-8
        # 8
        output = get_expression('8+8-2*32/2**3')
        assert output == 8

    def test_calculate_pEMDAS_two(self):
        # 4+80/2^3*2-8
        # 4+80/8*2-8
        # 4+10*2-8
        # 4+20-8
        # 24-8
        # 16
        output = get_expression('4+80/2^3*2-8')
        assert output == 16

    def teardown_method(self, method):
        """
        This method is being called after each test case, and it will revert
        input back to original function
        """
        calculator.input = input
