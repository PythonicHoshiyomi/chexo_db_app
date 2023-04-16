from django.urls import path, include, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from .models import Dojo, Member

def create_test_dojo(self) -> Dojo:
    url = reverse('dojo-add')
    data = {
        "dojo_name": "Dojo 1 "
    }
    self.client.post(url,data,format='json')

def create_test_member(self):
        create_test_dojo(self)
        data = {
            "name": "member",
            "birth_date": "2000-01-01",
            "kyu": 5
        }
        self.client.post(reverse('member-add', args=[1]), data=data, format="json")


class ApiTest(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('api.urls'))
    ]
    def test_dojo_list(self):
        url = reverse('dojo-list')
        response = self.client.get(url,format='json')
        self.assertEqual(response.status_code, 200)

    def test_create_dojo(self):
        url = reverse('dojo-add')
        data = {
            "dojo_name": "Dojo 1"
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Dojo.objects.all().count(), 1)
        self.assertEqual(Dojo.objects.get().dojo_name, "Dojo 1")

    def test_create_member_(self):
        response = self.client.post(reverse('dojo-add'), {"dojo_name": "Dojo"}, format='json')
        self.assertEqual(response.status_code, 200)
        data = {
            "name": "member",
            "birth_date": "2000-01-01",
            "kyu": 5
        }
        response = self.client.post(reverse('member-add', args=[1]), data=data, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Member.objects.all().count(), 1)
        self.assertEqual(Member.objects.get().name, "member")

    def test_update_dojo(self):
        create_test_dojo(self)
        url = reverse('dojo-update',args=[1])
        data = {
            "dojo_name": "Dojo 2"
        }
        response = self.client.put(url,data,format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Dojo.objects.get(pk=1).dojo_name, "Dojo 2")


    def test_update_member(self):
        create_test_dojo(self)
        create_test_member(self)
        data = {
            "dojo": 1,
            "name": "Udin",
            "birth_date": "2000-01-01",
            "kyu": 1
        }
        url = reverse('member-update', args=[1,1])
        response = self.client.put(url,data,format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Member.objects.all().count(), 1)
        self.assertEqual(Member.objects.get(dojo_id=1, pk=1).name, "Udin")

    def test_delete_dojo(self):
        create_test_dojo(self)
        url = reverse('dojo-delete', args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Dojo.objects.all().count(), 0)

    def test_delete_member(self):
        create_test_dojo(self)
        create_test_member(self)
        url = reverse('member-delete', args=[1,1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Member.objects.all().count(), 0)
