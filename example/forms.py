from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32,
        widget=forms.TextInput(attrs={'class' : 'form-control'}),
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
        widget=forms.TextInput(attrs={'class' : 'form-control'}),
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput(attrs={'class' : 'form-control'}),        
    )

class UserLoginForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32,
        widget=forms.TextInput(attrs={'class' : 'form-control'}),
    )    
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput(attrs={'class' : 'form-control'}),        
    )



class CheckOutForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Name',
        max_length = 64,
        widget=forms.TextInput(attrs={'class' : 'form-control'}),
    )
    address = forms.CharField(
        required = True,
        label = 'Address',
        max_length = 128,
        widget=forms.TextInput(attrs={'class' : 'form-control'}),
    )
    cardnumber = forms.CharField(
        required = True,
        label = 'CreditCard',
        max_length = 16,
        widget = forms.TextInput(attrs={'class' : 'form-control'}),        
    )
    cardmonth = forms.CharField(
        required = True,
        label = 'Expiration Month',
        max_length = 2,
        widget = forms.TextInput(attrs={'class' : 'form-control'}),        
    )
    cardyear = forms.CharField(
        required = True,
        label = 'Expiration Year',
        max_length = 2,
        widget = forms.TextInput(attrs={'class' : 'form-control'}),        
    )
    cardsc = forms.CharField(
        required = True,
        label = 'Security Code',
        max_length = 3,
        widget = forms.TextInput(attrs={'class' : 'form-control'}),        
    )