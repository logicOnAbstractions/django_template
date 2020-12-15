from django.shortcuts import render, HttpResponseRedirect
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

def create_product(request):
    if request.method == "POST":
        form = CreateElement(request.POST)
        if form.is_valid():
            # create a product
            p = MyObjects(**form.cleaned_data)
            p.save()

            return HttpResponseRedirect('/myapp/listview')       # let's say go back to product list or something
    else:
        form = CreateElement()
    return render(request, 'myapp/createlistelement.html', {'form': form})