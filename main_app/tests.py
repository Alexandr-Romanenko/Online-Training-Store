from django.test import TestCase
from main_app.models import CustomUser, Product, Purchase, Returns

# Create your tests here.


class CustomUserTest(TestCase):
    """ Test module for CustomUser model """

    def setUp(self):
        CustomUser.objects.create(
            username='cucumber', password='RedBull23', wallet=9500.0)
        CustomUser.objects.create(
            username='tarzan', password='RedTomato23', wallet=10000.0)

    def test_custom_user_model_fields(self):
        custom_user_cucumber = CustomUser.objects.get(username='cucumber')
        custom_user_tarzan = CustomUser.objects.get(username='tarzan')
        self.assertEqual(
            custom_user_cucumber.get_username(), "cucumber")
        self.assertEqual(
            custom_user_tarzan.get_username(), "tarzan")
        self.assertEqual(
            custom_user_cucumber.wallet, 9500.0)
        self.assertEqual(
            custom_user_tarzan.wallet, 10000.0)


