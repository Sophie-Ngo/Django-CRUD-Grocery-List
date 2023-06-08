from django import forms
from .models import Groceries

# A form can be re-used. This form is not specific to any one CRUD operation because 
# it simply defines what model, and which fields of that model are to be displayed in the form.
class GroceriesForm(forms.ModelForm):

    class Meta:
        model = Groceries
        fields = ['name', 'quantity',]

    # remember: ModelForm has a save method. it creates and saves a db object
    # from the data bound to the form. There is no save() to be done yourself.

