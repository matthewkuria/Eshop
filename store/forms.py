from django import forms

class CheckoutForm(forms.Form):
    address = forms.CharField(max_length=255, required=True)
    city = forms.CharField(max_length=100, required=True)
    state = forms.CharField(max_length=100, required=True)
    zip_code = forms.CharField(max_length=10, required=True)
    payment_method = forms.ChoiceField(choices=[('card', 'Credit/Debit Card'), ('paypal', 'PayPal')])
    card_number = forms.CharField(max_length=16, required=False)
    expiry_date = forms.CharField(max_length=5, required=False)
    cvv = forms.CharField(max_length=3, required=False)
