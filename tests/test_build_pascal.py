import pytest
from modules.utils.build_pascal import build_triangle

@pytest.fixture
def init_pascal():
	pascal = build_triangle()
	yield pascal

""" These tests are meant to prove that the utility function for building the Pascal Triangle works. """
def test_pascal_triangle_row_1(init_pascal):
	pascal_triangle = init_pascal
	row_1 = pascal_triangle[0]
	assert row_1 == [1]

def test_pascal_triangle_row_3(init_pascal):
	pascal_triangle = init_pascal
	row_3 = pascal_triangle[2]
	assert row_3 == [1, 2, 1]

def test_pascal_triangle_row_5(init_pascal):
	pascal_triangle = init_pascal
	row_5 = pascal_triangle[4]
	assert row_5 == [1, 4, 6, 4, 1]

def test_pascal_triangle_row_7(init_pascal):
	pascal_triangle = init_pascal
	row_7 = pascal_triangle[6]
	assert row_7 == [1, 6, 15, 20, 15, 6, 1]
