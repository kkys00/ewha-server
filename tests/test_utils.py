"""
Test code
"""
from main import total


def test_total_success():
    """
    total 함수 정상 동작 테스트
    """
    assert total(2, 3) == 5
