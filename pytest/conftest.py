import pytest


@pytest.fixture
def my_fixture():
	return 42


@pytest.fixture
def capture_print(capsys):
	print("hello")