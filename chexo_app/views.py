from django.shortcuts import render
from .models import MemberList, DojoList
from django.views import generic
from django.urls import reverse

class ListListView(generic.ListView):
    model = DojoList 
    template_name = "chexo_app/index.html"

class MemberListView(generic.ListView):
    model = MemberList
    template_name = "chexo_app/member_list.html"

    def get_queryset(self):
        return MemberList.objects.filter(dojo_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["dojo_list"] = MemberList.objects.get(id=self.kwargs["list_id"])
        return context

class ListCreate(generic.CreateView):
    model = DojoList
    fields = ["dojo_name"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add a new Dojo"
        return context
    