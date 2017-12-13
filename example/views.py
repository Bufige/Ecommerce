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
from pagseguro.api import PagSeguroItem, PagSeguroApi
# Create your views here.



class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		

		products = Products.objects.all()
		cart = Cart(request)

		cart_total = self.request.session.get('cart_total',0)
		self.request.session['cart_total'] = cart.total()		



		return render(request,'index.html', {'products': products})	





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
					return redirect('home')
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
                return redirect('home')
            
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form' : form})



def AddCart(request,id):
	
	product = Products.objects.filter(id=id).values('title','id','price')[0]
	
	cart = Cart(request)
	
	cart.add(product,update = True)	


	return redirect('home')

def CartPageView(request):

	cart = Cart(request)
	pagseguro_api = PagSeguroApi(reference='2309238123939293')

	if request.method == 'POST':

		for item in cart.getall():
			print(item)
			pag_item = PagSeguroItem(id= item['id'], description= item['title'] , amount= item['price'], quantity= item['quantity'], shipping_cost='25.00', weight=500)
			pagseguro_api.add_item(pag_item)
		data = pagseguro_api.checkout()
		return redirect(data['redirect_url'])

	return render(request, 'cart.html', {'products' : cart.getall(), 'totalprice' : cart.totalprice() })


@login_required(login_url='/login')
def CheckOutPageView(request):
	cart = Cart(request)
	if cart.total() == 0:
		return redirect('cart')
	#return bait()

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


@login_required(login_url='/login')
def SuccessPageView(request):
	cart = Cart(request)
	if cart.total() == 0:
		return redirect('home')
	cart.clear()
	return render(request, 'success.html')