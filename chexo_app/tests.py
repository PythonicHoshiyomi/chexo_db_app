from django.test import TestCase
from django.urls import reverse
from .models import DojoList, MemberList

def create_dojo(dojo_name: str) -> DojoList:
    return DojoList.objects.create(dojo_name=dojo_name)

def create_member(name:str, birth_date:str, kyu:int, dojo:DojoList) -> MemberList:
    return dojo.memberlist_set.create(name=name, birth_date=birth_date, kyu=kyu)

def delete_member(dojo:DojoList, member:MemberList) -> None:
    return dojo.memberlist_set.get(id=member.id).delete()

def delete_dojo(dojo:DojoList) -> None:
    return DojoList.objects.get(id=dojo.id).delete()
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
        If no member exists, an appropriate message is displayed.
        """
        dojo = create_dojo("test")
        response = self.client.get(dojo.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response=response, text="You have no member")
        self.assertQuerysetEqual(response.context['object_list'], [])

    def test_create_a_member(self):
        """
        New member is displayed on the Dojo list.
        """
        dojo = create_dojo("test dojo")
        member = create_member("Test", "2001-01-01", 8, dojo)
        response = self.client.get(dojo.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['object_list'], [member])

    def test_delete_a_member(self):
        """
        Dojo is no longer displayed on the index page.
        """
        dojo = create_dojo("Dojo1")
        member = create_member("Member1", "2000-01-01", 8, dojo)
        delete_member(dojo, member)
        response = self.client.get(dojo.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['object_list'], [])

    def test_delete_a_dojo(self):
        """
        Member is no longer displayed on the Dojo list page.
        """
        dojo = create_dojo("Dojo1")
        delete_dojo(dojo=dojo)
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response=response, text="No Dojo available")
        self.assertQuerysetEqual(response.context['object_list'], [])