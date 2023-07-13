from django.shortcuts import redirect, reverse
from django.http import HttpResponseRedirect, request
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Groceries
from .forms import GroceriesForm

# api imports
from rest_framework import generics
from .serializers import GroceriesSerializer

# Lists all groceries in alphabetical order.
class GroceriesListView(ListView):
    model = Groceries
    template_name = 'groceryapp/grocerieslist.html'
    context_object_name = 'groceries'

    # order by name - sorts the list alphabetically.
    # without order by, this method would do the same 
    # as default
    def get_queryset(self):
        return Groceries.objects.all().order_by('name')

# GET - show info about a single grocery
class GroceriesDetailView(DetailView):
    template_name ='groceryapp/grocery.html'
    model = Groceries

# CREATE - create a new grocery
class GroceriesCreateView(CreateView):
    form_class = GroceriesForm
    template_name = 'groceryapp/groceriescreate.html'
    model = Groceries
    success_url = '/groceryapp/'

class GroceriesUpdateView(UpdateView):
    model = Groceries
    form_class = GroceriesForm
    template_name = 'groceryapp/groceriesupdate.html'

    def form_valid(self, form):
        data = form.save()
        next_url = self.request.POST.get('next')

        return HttpResponseRedirect(reverse(next_url, args=[data.pk]))

class GroceriesDeleteView(DeleteView):
    model = Groceries
    template_name = 'groceryapp/groceriesdelete.html'
    success_url = '/groceryapp/'


# ------------- api stuff ------------- #

# endpoint for getting all groceries as a list
class GroceriesListApi(generics.ListCreateAPIView):
    serializer_class = GroceriesSerializer

    def get_queryset(self):
        queryset = Groceries.objects.all()
        return queryset
    
# endpoint for getting detail of a specific grocery
class GroceriesDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroceriesSerializer
    queryset = Groceries.objects.all()