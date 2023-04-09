from django.test import TestCase
from django.urls import reverse
from .models import DojoList, MemberList

def create_dojo(dojo_name: str):
    return DojoList.objects.create(dojo_name=dojo_name)

class DojoIndexViewTests(TestCase):

    def test_no_dojo(self):
        """
        if no Dojo exists, an appropriate message is displayed
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response=response, text="No Dojo available")
        self.assertQuerysetEqual(response.context['object_list'], [])

    def test_create_dojo(self):
        """
        Dojo is displayed on the index page.
        """
        dojo = create_dojo("test")
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['object_list'], [dojo])
        
    def test_no_dojo_member(self):
        """
        If no member exists, an appropriate message is displayed
        """
        dojo = create_dojo("test")
        response = self.client.get(dojo.pk)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response=response, text="You have no member")
        self.assertQuerysetEqual(response.context['object_list'], [])
