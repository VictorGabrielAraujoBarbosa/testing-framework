from TestCase import TestCase


# classes mockadas para representar um teste real
class TestStub(TestCase):

    def test_success(self):
        assert True

    def test_failure(self):
        assert False

    def test_error(self):
        raise Exception
    
class TestSpy(TestCase):

    def __init__(self, name):
        TestCase.__init__(self, name)
        self.was_run = False
        self.was_set_up = False
        self.was_tear_down = False
        self.log = ""

    def set_up(self):
        self.was_set_up = True
        self.log += "set_up "

    def test_method(self):
        self.was_run = True
        self.log += "test_method "

    def tear_down(self):
        self.was_tear_down = True
        self.log += "tear_down"
    