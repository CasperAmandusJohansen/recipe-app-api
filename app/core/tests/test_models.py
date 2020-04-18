from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """
    Test class
    """

    def test_create_user_with_email_successfull(self):
        """
        Test creating a new user iwht an email is successfull
        """

        email = 'test@test.com'
        password = 'Testpass1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """
        Test email for a new user is normalized
        """
        email = 'test@TEST.com'
        user = get_user_model().objects.create_user(email,'test321')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """
        Test creating a user with no email raises error
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'123')

    def test_create_new_superuser(self):
        """
        Test creating a new superuser
        """

        user = get_user_model().objects.create_superuser('test@test.com', 'Test321')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)