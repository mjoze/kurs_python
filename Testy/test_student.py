import unittest
from student import Student


class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('######setUpClass#######\n')

    @classmethod
    def tearDownClass(cls):
        print('######tearDownClass#######\n')

    def setUp(self):
        print('setUp')
        self.obj_anna = Student('anna', 'kowalska', 4.6, None)
        self.obj_arek = Student('arkadiusz', 'nowak', 3.8, None)

    def tearDown(self):
        print('tearDown')
        print('###############')

    def test_email(self):
        print('email')
        self.assertEqual(self.obj_anna.email, 'anna.kowalska@university.com')

        self.obj_anna.name = 'joanna'
        self.assertEqual(self.obj_anna.email, 'joanna.kowalska@university.com')

    def test_fullname(self):
        print('fullname')
        self.assertEqual(self.obj_anna.fullname, 'Anna Kowalska')
        self.obj_anna.last = 'borowiec'
        self.assertEqual(self.obj_anna.fullname, 'Anna Borowiec')

    def test_grant_scholarship(self):
        print('scholarship')
        self.obj_anna.grant_scholarship()
        self.assertEqual(self.obj_anna.scholarship, True)

        self.obj_arek.grant_scholarship()
        self.assertEqual(self.obj_arek.scholarship, False)


if __name__ == 'main':
    unittest.main()
