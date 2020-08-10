import pytest
import random
import string
import session4
import os
import inspect
import re
import math, cmath
import decimal
from decimal import Decimal
import random
import itertools

# random.seed(101)

decimal.getcontext().prec = 10

README_CONTENT_CHECK_FOR = [
    'Qualean',
    "Banker's",
    'rounding',
    'precision',
    '__and__',
    '__or__',
    '__repr__',
    '__str__',
    '__add__',
    '__eq__',
    '__float__',
    '__ge__',
    '__gt__',
    '__invertsign__',
    '__le__',
    '__lt__',
    '__mul__',
    '__sqrt__',
    '__bool__'
]

CHECK_FOR_IMPLEMENTED_FUNCTIONS = [
    '__and__',
    '__or__',
    '__repr__',
    '__str__',
    '__add__',
    '__eq__',
    '__float__',
    '__ge__',
    '__gt__',
    '__invertsign__',
    '__le__',
    '__lt__',
    '__mul__',
    '__sqrt__',
    '__bool__'
]


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_requirement_file_exists():
    assert os.path.isfile("requirements.txt"), "requirements.txt file missing!"


def test_readme_contents():
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add at least 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD is True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session4)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_things_implemented():
    code_lines = inspect.getsource(session4)
    implemented_flag = True
    for item in CHECK_FOR_IMPLEMENTED_FUNCTIONS:
        if item not in code_lines:
            implemented_flag = False
            break
    assert implemented_flag is True, 'You forgot to implement all methods!'


def test_decimal_used_or_not():
    code_lines = inspect.getsource(session4)
    assert 'decimal' in code_lines, 'Decimal not used! '
    assert 'import' in code_lines, 'You have not imported anything!'


def test_add():
    for _ in range(10):
        l = [1, 0, -1, 1.0, -1.0]
        for num in l:
            q = session4.Qualean(num)
            sum = Decimal('0')
            for i in range(100):
                sum = sum + q.value
            assert math.isclose(sum, 100 * q.value, rel_tol=1e-5, abs_tol=0.0) is True


def test_for_bool():
    l = [0, -1, 1, 1.0, -1.0]
    for num in l:
        q = session4.Qualean(num)
        assert q.__bool__() == (q.value != 0)


def test_invert_sign():
    l = [1, -1]
    for num in l:
        q = session4.Qualean(num)
        assert q.__invertsign__() == -1 * q.value


# def test_sqrt():
#     for _ in range(100):
#         l = [1, -1, 0]
#         for num in l:
#             q = session4.Qualean(num)
#             sqrt = q.__sqrt__()
#             num_sqrt = cmath.sqrt(q.value)
#             assert cmath.isclose(sqrt, num_sqrt, rel_tol=1e-2, abs_tol=0.0)

def test_sqrt():
    for _ in range(1000):
        l = [1, 0, -1, 1.0, -1.0]
        for num in l:
            q = session4.Qualean(num)
            if q.value >= 0:
                assert q.__sqrt__() == Decimal.sqrt(q.value)
            else:
                assert q.__sqrt__() == cmath.sqrt(q.value)

                # assert cmath.isclose(q.__sqrt__(), cmath.sqrt(q.value), rel_tol=1e-5)


def test_eq():
    sum = 0
    any = random.choice([1, 0, -1, 1.0, -1.0])
    for i in range(1000000):
        q = session4.Qualean(any)
        sum = sum + q.value
    assert sum.__eq__(0) == math.isclose(sum, 0)
    l = list(itertools.combinations_with_replacement([1, 0, -1], 2))
    for a, b in l:
        # session4.set_seed(101)
        q1 = session4.Qualean(a)
        q2 = session4.Qualean(b)
        assert q1.__eq__(q2) == (math.isclose(q1.value, q2.value, rel_tol=1e-5, abs_tol=0.0))


def test_function_for_gt():
    a = random.choice([1, 0, -1, 1.0, -1.0])
    b = random.choice([1, 0, -1, 1.0, -1.0])
    q1 = session4.Qualean(a)
    q2 = session4.Qualean(b)
    assert (q1.__gt__(q2)) == (q1.value > q2.value)


def test_function_for_lt():
    a = random.choice([1, 0, -1, 1.0, -1.0])
    b = random.choice([1, 0, -1, 1.0, -1.0])
    q1 = session4.Qualean(a)
    q2 = session4.Qualean(b)
    assert (q1.__lt__(q2)) == (q1.value < q2.value)


def test_function_for_le():
    a = random.choice([1, 0, -1, 1.0, -1.0])
    b = random.choice([1, 0, -1, 1.0, -1.0])
    q1 = session4.Qualean(a)
    q2 = session4.Qualean(b)
    assert (q1.__le__(q2)) == (q1.value <= q2.value)


def test_function_for_ge():
    a = random.choice([1, 0, -1, 1.0, -1.0])
    b = random.choice([1, 0, -1, 1.0, -1.0])
    q1 = session4.Qualean(a)
    q2 = session4.Qualean(b)
    assert (q1.__ge__(q2)) == (q1.value >= q2.value)


def test_mul():
    for _ in range(10):
        a = random.choice([1, 0, -1, 1.0, -1.0])
        b = random.choice([1, 0, -1, 1.0, -1.0])
        q1 = session4.Qualean(a)
        q2 = session4.Qualean(b)
        assert q1.__mul__(q2) == (q1.value * q2.value)


def test_or():
    for _ in range(10):
        a = random.choice([1, 0, -1, 1.0, -1.0])
        b = random.choice([1, 0, -1, 1.0, -1.0])
        q1 = session4.Qualean(a)
        q2 = session4.Qualean(b)
        assert q1.__or__(q2) == bool(q1.value or q2.value)


def test_and():
    for _ in range(10):
        a = random.choice([1, 0, -1, 1.0, -1.0])
        b = random.choice([1, 0, -1, 1.0, -1.0])
        q1 = session4.Qualean(a)
        q2 = session4.Qualean(b)
        assert q1.__and__(q2) == bool(q1.value and q2.value)


def test_float():
    for _ in range(10):
        a = random.choice([1, 0, -1, 1.0, -1.0])
        q = session4.Qualean(a)
        assert q.__float__() == float(q.value)


def test_repr():
    a = random.choice([1, 0, -1, 1.0, -1.0])
    b = random.choice([1, 0, -1, 1.0, -1.0])
    q1 = session4.Qualean(a)
    q2 = session4.Qualean(b)
    assert (type(eval(repr(q1))) == str and type(eval(repr(q2))) == str) and 'object at' not in q1.__repr__() and 'object at' not in q2.__repr__()


def test_str():
    a = random.choice([1, 0, -1, 1.0, -1.0])
    b = random.choice([1, 0, -1, 1.0, -1.0])
    q1 = session4.Qualean(a)
    q2 = session4.Qualean(b)
    assert '<__main__.Qualean object at' not in q1.__str__() and '<__main__.Qualean object at' not in q2.__str__()


def test_ne():
    a = random.choice([1, 0, -1, 1.0, -1.0])
    b = random.choice([1, 0, -1, 1.0, -1.0])
    q1 = session4.Qualean(a)
    q2 = session4.Qualean(b)
    assert q1.__ne__(q2) == (q1.value != q2.value)


# def test_prec():
#     for _ in range(100):
#         q_prec = len(str(session4.Qualean(random.choice([1, -1, 1.0, -1.0]))).split('.')[1])
#         assert q_prec == 10


def test_context_usage():
    code_lines = inspect.getsource(session4)
    assert 'context' in code_lines, "Decimal's context not used! "


def test_not_implemented():
    for num in [1, 0, -1, 1.0, -1.0]:
        q = session4.Qualean(num)
        m = [int, float, bool, str, complex, tuple, list, dict, set]
        for t in m:
            for method in [session4.Qualean.__add__, session4.Qualean.__mul__, session4.Qualean.__gt__,
                           session4.Qualean.__ge__, session4.Qualean.__lt__,
                           session4.Qualean.__le__, session4.Qualean.__eq__]:
                assert method(q, t()) == NotImplemented


def test_random_uniform_usage():
    code_lines = inspect.getsource(session4)
    assert 'random.uniform(-1, 1)' in code_lines, "random.uniform not used! "


