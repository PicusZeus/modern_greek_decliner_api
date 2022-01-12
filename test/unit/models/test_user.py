from models.user import UserModel
from test.unit.unit_base_test import UnitBaseTest


class UserTest(UnitBaseTest):

    def test_create_user(self):
        user = UserModel('albert@op.pl', 'albert', '123', 3333)

        self.assertEqual(user.password, '123')
        self.assertEqual(user.password, '123')
        self.assertEqual(user.username, 'albert')
        self.assertEqual(user.phoneNumber, 3333)
