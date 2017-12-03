from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from django import forms
from .forms import *
from django.forms.models import model_to_dict
from .models import Products
from .cart.cart import Cart
# Create your views here.



class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		

		products = Products.objects.all()
		cart = Cart(request)

		cart_total = self.request.session.get('cart_total',0)
		self.request.session['cart_total'] = cart.total()		



		return render(request,'index.html', {'products': products})	

class AboutPageView(TemplateView):
	template_name = 'about.html'





@login_required(login_url='/login')
def ProfilePageView(request):
	return render(request,'profile.html',context=None)

def UserLogin(request):
	
	if request.POST:
		form = UserLoginForm(request.POST)
		if form.is_valid():
			userObj = form.cleaned_data
			username = userObj['username']
			password = userObj['password']

			user = authenticate(username = username, password = password)

			if user:
				if user.is_active:
					login(request,user)
					return redirect('/')
	else:
		form = UserLoginForm()
	
	return render(request,'registration/login.html', {'form' : form})



def UserSignUp(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return redirect('/')
            
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form' : form})



def AddCart(request,id):
	
	product = Products.objects.filter(id=id).values('title','id','price')[0]
	
	cart = Cart(request)
	
	cart.add(product,update = True)	


	return redirect('/')

def CartPageView(request):

	cart = Cart(request)
	return render(request, 'cart.html', {'products' : cart.getall(), 'totalprice' : cart.totalprice() })


@login_required(login_url='/login')
def CheckOutPageView(request):
	if request.method == 'POST':
		form = CheckOutForm()
		if form.is_valid():
			userObj = form.cleaned_data
			username = userObj['username']
			email = userObj['email']
			creditcard = userObj['creditcard']
	else:
		form = CheckOutForm()	
	cart = Cart(request)
	return render(request, 'checkout.html', {'form' : form , 'products' : cart.getall(), 'totalprice' : cart.totalprice() })