from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from main.models import Menu, Order
from user.models import MyUser
from django.utils.timezone import localtime


# Test to verify if url respond correctly
class HomePageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home_main'))
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home_main'))
        self.assertEquals(response.status_code, 200)


# Testing post in models Menu and Order
class MenuTests(TestCase):

    def setUp(self):
        # create objects user and menu
        self.user = MyUser.objects.create_superuser(
            username='usertest',
            email='user1111@example.com',
            password='user1111',
            employee=False,
            country='Chile',
            jobs='Developers'

        )
        self.menu = Menu.objects.create(
            starter='Salads',
            main_course='Chop Suey',
            desserts='Ice Cream',
            menu_date=localtime(),
            owner=self.user
        )

    def test_text_content(self):
        menu = Menu.objects.get(id=1)
        expected_object_name = menu
        self.assertEquals(expected_object_name, self.menu)

    def test_menu_list_view(self):
        self.client.login(
            username='usertest',
            password='user1111'
        )
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/list_menu.html')


class OrderTests(TestCase):
    def setUp(self):
        # create objects user,menu and order
        self.user = MyUser.objects.create_user(
            username='user_employee',
            email='user1111@example.com',
            password='user1111',
            employee=True,
            country='Chile',
            jobs='Developers'

        )
        self.menu = Menu.objects.create(
            starter='Salads',
            main_course='Chop Suey',
            desserts='Ice Cream',
            menu_date=localtime(),
            owner=self.user
        )

        self.order = Order.objects.create(
            menu=self.menu,
            customization='Staterd without tomatoes',
            employee=self.user
        )

    def test_text_content(self):
        # get order created
        order = Order.objects.get(id=1)
        expected_object_name = order
        self.assertEquals(expected_object_name, self.order)

    def test_order_list_view(self):
        self.client.login(
            username='user_employee',
            password='user1111'
        )
        response = self.client.get(reverse('order_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/list_order.html')
