from .models import MemberList, DojoList
from django.views import generic
from django.urls import reverse, reverse_lazy


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
        context["dojo_list"] = DojoList.objects.get(id=self.kwargs["list_id"])
        return context


class ListCreate(generic.CreateView):
    model = DojoList
    fields = ["dojo_name"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add a new Dojo"
        return context


class MemberCreate(generic.CreateView):
    model = MemberList
    fields = [
        "name",
        "dojo",
        "birth_date",
        "kyu",
    ]

    def get_initial(self):
        initial_data = super().get_initial()
        dojo = DojoList.objects.get(id=self.kwargs["list_id"])
        initial_data["dojo"] = dojo
        return initial_data

    def get_context_data(self):
        context = super().get_context_data()
        dojo = DojoList.objects.get(id=self.kwargs["list_id"])
        context["dojo"] = dojo
        context["title"] = "Add a new member"
        return context

    def get_success_url(self) -> str:
        return reverse("list", args=[self.object.dojo_id])


class MemberUpdate(generic.UpdateView):
    model = MemberList
    fields = [
        "name",
        "dojo",
        "birth_date",
        "kyu",
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dojo"] = self.object.dojo
        context["title"] = "Edit member"
        return context

    def get_success_url(self) -> str:
        return reverse("list", args=[self.object.dojo_id])


class DojoUpdate(generic.UpdateView):
    model = DojoList
    fields = ["dojo_name"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Dojo name"
        return context

    def get_success_url(self) -> str:
        return reverse("list", args=[self.object.id])


class DojoDelete(generic.DeleteView):
    model = DojoList
    success_url = reverse_lazy("index")


class MemberDelete(generic.DeleteView):
    model = MemberList

    def get_success_url(self) -> str:
        return reverse_lazy("list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dojo"] = self.object.dojo
        return context