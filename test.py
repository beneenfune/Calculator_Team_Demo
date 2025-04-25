from Calculator import Calculator

calc = Calculator()

def test_add():
    if calc.add(1, 2) == 3 and calc.add(-1, 5) == 4:
        print("add: PASS")
    else:
        print("add: FAIL")

def test_subtract():
    if calc.subtract(5, 2) == 3 and calc.subtract(0, 4) == -4:
        print("subtract: PASS")
    else:
        print("subtract: FAIL")

def test_multiply():
    if calc.multiply(3, 4) == 12 and calc.multiply(-1, 5) == -5:
        print("multiply: PASS")
    else:
        print("multiply: FAIL")

def test_divide():
    if calc.divide(10, 2) == 5 and calc.divide(5, 2) == 2.5:
        print("divide: PASS")
    else:
        print("divide: FAIL")

def test_square():
    if calc.square(3) == 9 and calc.square(-2) == 4:
        print("square: PASS")
    else:
        print("square: FAIL")

def test_cube():
    if calc.cube(2) == 8 and calc.cube(-3) == -27:
        print("cube: PASS")
    else:
        print("cube: FAIL")

# Run all tests
test_add()
test_subtract()
test_multiply()
test_divide()
test_square()
test_cube()

