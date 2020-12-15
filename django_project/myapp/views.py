from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views import generic
from .models import *
from .forms import *
from django import forms


class IndexView(generic.View):
    template_name = 'myapp/index.html'
    context_object_name = 'dummy'

    def get(self, request):
        return render(request, self.template_name)


class MyListView(generic.ListView):
    template_name = 'myapp/mylistview.html'
    model = MyObjects
    context_object_name = 'objects'


class ListElementView(generic.DetailView):
    model = MyObjects
    template_name = 'myapp/list_element.html'

class ObjectCreate(generic.CreateView):
    template_name = 'myapp/createlistelement.html'
    model = MyObjects
    fields = ["name"]

    def get_success_url(self):
        return reverse('myapp:mylistview')

