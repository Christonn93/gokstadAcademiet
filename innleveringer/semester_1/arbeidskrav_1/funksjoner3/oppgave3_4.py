def test_function(func, args, expected_result):

    try:
        result = func(*args)
        return result == expected_result

    except Exception as e:
        print(f"Error occurred: {e}")
        return False

def add(a, b):
    return a + b

def multiply(x, y):
    return x * y

def main():
    print(test_function(add, (2, 3), 5))
    print(test_function(multiply, (4, 5), 20))
    print(test_function(add, (2, '3'), 5))