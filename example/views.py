from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


from .models import Products
# Create your views here.



class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		#self.AddData()

		products = Products.objects.all()

		return render(request,'index.html', {'Products': products})
	def AddData(self):
		#obj = Products.objects.create(title='colt 45 1911', imagePath='http://www.coltautos.com/images/1911_Navy_109967i.jpg' , description='Good weapon to shoot at niggas and faggots', price = 475)
		pass

class AboutPageView(TemplateView):
	template_name = 'about.html'

@login_required(login_url='/login')
def ProfilePageView(request):
	return render(request,'profile.html',context=None)

def UserSignUp(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username,password=password)
			login(request,user)
			return redirect('/')
	else:
		form = UserCreationForm()
	return render(request,'registration/register.html', {'form' : form})



