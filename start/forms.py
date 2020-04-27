from django import forms
from start.models import Order, Coffee

class OrderForm(forms.ModelForm):
    order_name = forms.ModelChoiceField(queryset=Coffee.objects.all(), widget=forms.HiddenInput)

    class Meta:
        model = Order
        fields = ('order_name', 'name', 'phone' )


