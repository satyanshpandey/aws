from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from django.views import View

# Create your views here.
class Index(View):
	
	#For Handle POST Request
	def post( self , request ):
		product = request.POST.get('product')
		remove = request.POST.get('remove')
		cart = request.session.get('cart')
		if cart:
			quantity = cart.get(product)
			if quantity:
				if remove:
					if quantity==1:
						cart.pop(product)
					else:
						cart[product] = quantity-1
				else:
					cart[product] = quantity+1
			else:
				cart[product] = 1
		else:
			cart = {}
			cart[product] = 1
			
		request.session['cart'] = cart
		print('cart',request.session['cart'])
		#print(product)
		print("hey guys this is satyansh pandey",request.session['cart'])
		return redirect('homepage')
	
	
	#For handle Get Request
	def get( self , request):
		
		cart = request.session.get('cart')
		if not cart:
			request.session['cart'] = {}
		
		products = None
		#request.session.get('cart').clear()
		categories = Category.get_all_categories ( )
		# print(prds)
		categoryID = request.GET.get ( 'category' )
		if categoryID :
			products = Product.get_all_products_by_categoryid ( categoryID )
		else :
			products = Product.get_all_products ( ) ;
		
		data = { }
		data [ 'products' ] = products
		data [ 'categories' ] = categories
		print ( "You are: " , request.session.get('email'))
		return render( request , 'index.html' , data )