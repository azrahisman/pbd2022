from django import forms

class WishlistForm(forms.Form):
    item_name = forms.CharField(label='Item Name', max_length=50)
    item_price = forms.IntegerField(label='Item Price')
    description = forms.CharField()
