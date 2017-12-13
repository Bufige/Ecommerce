from decimal import Decimal 
from django.conf import settings
from ..models import Products


class Cart(object):
	def __init__(self,request):
		self.session = request.session
		cart = self.session.get(settings.CART_SESSION_ID)




		if not cart:
			cart = self.session[settings.CART_SESSION_ID] = {}
		else:
			pass
		self.cart = cart
	

	def add(self, product, quantity = 1, update = False):
		product_id = str(product['id'])

		if product_id not in self.cart:
			self.cart[product_id] = {'quantity':0, 'price' : str(product['price']), 'title': product['title'], 'id' : product_id}
		if not update:
			self.cart[product_id]['quantity'] = quantity
		else:
			self.cart[product_id]['quantity'] += quantity

		self.session[settings.CART_SESSION_ID] = self.cart
		
		self.session.modified = True
	
	def get(self, product_id):
		product_id = str(product_id)
		if product_id in self.cart:
			return self.cart[product_id]
		return None

	def getall(self):
		return self.cart.values()

	def total(self):
		amount = 0
		for item in self.cart.values():			
			amount += item['quantity']			
		return amount

	def totalprice(self):
		totalprice = 0
		for item in self.cart.values():
			totalprice += item['quantity'] * Decimal(item['price'])
		return totalprice
		
	def clear(self):
		del self.session[settings.CART_SESSION_ID]
		self.session.modified = True