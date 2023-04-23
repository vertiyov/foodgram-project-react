from users.models import User
from django.test import TestCase

class UserModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user=User.objects.create(
            first_name='Vl',
            last_name = 'V',
            email = 'asd@ta.ru',
            username = 'bigbiVlVlVlVlVlVlVlVlVlVlVlVlVlVlVlVlVlVlVlVlVlVlVlVlVlVlVlVlVlVlVlVly',
            password = 'sdfsdf222',
        )

    def test_userrr(self):
        """Содержимое поля title преобразуется в slug."""
        user = UserModelTest.user
        print(user.username)
        self.assertEqual(user.first_name, 'Vl')
