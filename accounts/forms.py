from django.forms import ModelForm
from .models import OrderMod, CustomerMod

class OrderForm(ModelForm):
    class Meta:
        model = OrderMod
        fields ='__all__' #Using all the fields of the model.


class CustomerForm(ModelForm):
    class Meta:
        model = CustomerMod
        fields = ['name','phone']