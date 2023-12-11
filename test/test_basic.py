from evostats.basic import add

class Test_add:
    def test_basic(self):
        x = 1
        y = 2
        assert add(x,y) == 3
