from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from .models import Women


class GetPagesTestCase(TestCase):
    fixtures = ["women_women.json", "women_category.json", "women_husband.json", "women_tagpost.json", "users_user.json"]

    def setUp(self):
        return super().setUp()
    
    def test_main_page(self):
        path = reverse("home")
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "women/index.html")
        self.assertEqual(response.context_data["title"], "Главная страница")


    def test_redirect_add_page(self):
        path = reverse("add_page")
        redirect_url = reverse("users:login") + "?next=" + path
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, redirect_url)

    def test_data_mainpage(self):
        w = Women.published.all().select_related("cat")
        path = reverse("home")
        response = self.client.get(path)
        print(w)

    def test_case_2(self):
        pass

    def tearDown(self):
        return super().tearDown()