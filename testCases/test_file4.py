import pytest


class Test_004:

    @pytest.mark.group1

    def test_mul_006(self):
        x = 5
        y = 7
        mul = x * y
        if mul == 35:
            assert True
        else:
            assert False