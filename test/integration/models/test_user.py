from test.integration.base_integration import BaseIntegrationTest
from models.user import UserModel


class User(BaseIntegrationTest):



    def test_crud(self):
        with self.app_context:
            user = UserModel('mail@com.pl', 'user_name', 'password', 444444444)
            user.insert()
            user_inst_1 = UserModel.find_by_email("mail@com.pl")
            user_inst_2 = UserModel.find_by_id(1)
            user_inst_3 = UserModel.find_by_username("user_name")
            self.assertEqual(user, user_inst_1)
            self.assertEqual(user, user_inst_2)
            self.assertEqual(user, user_inst_3)

            self.assertEqual('user_name', user_inst_1.username)
            self.assertEqual('password', user_inst_2.password)
            self.assertEqual(1, user_inst_3.id)

            print(user)

    def test_duplication(self):
        with self.app_context:
            user1 = UserModel('mail@com.pl', 'user_name', 'password', 444444444)
            user2 =UserModel('mail@com.pl', 'user_name', 'password', 444444444)

            user1.insert()
            user2.insert()
            users = UserModel.query.filter_by(username='user_name')


