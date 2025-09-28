from django.shortcuts import render , redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup ( View ) :
	def get ( self , request ) :
		return render ( request , 'signup.html' )
	
	def post ( self , request ) :
		
		postData = request.POST
		first_name = postData.get ( 'firstname' )
		last_name = postData.get ( 'lastname' )
		phone = postData.get ( 'phone' )
		email = postData.get ( 'email' )
		password = postData.get ( 'password' )
		# Validation
		
		value = {
			'first_name' : first_name ,
			'last_name' : last_name ,
			'phone' : phone ,
			'email' : email
		}
		
		error_message = None
		
		# Create Object of the 'CUSTOMER class' for save 'form data' into database table.
		customer = Customer (
			first_name=first_name ,
			last_name=last_name ,
			phone=phone ,
			email=email ,
			password=password )
		error_message = self.validateCustomer ( customer )
		
		# saving
		if not error_message :
			print ( first_name , last_name , phone , email , password )
			# here we are hashing our password before saving password!!!
			customer.password = make_password ( customer.password )
			customer.register ( )
			return redirect ( 'homepage' )
		# return render(request , 'index.html')
		else :
			data = {
				'error' : error_message ,
				'values' : value
			}
			return render ( request , 'signup.html' , data )
	
	def validateCustomer ( self , customer ) :
		error_message = None ;
		# First name validation
		if (not customer.first_name) :
			error_message = "First Name Required!!"
		elif len ( customer.first_name ) < 4 :
			error_message = "First Name must be 4 char!!"
		# Last name validation
		elif (not customer.last_name) :
			error_message = "Last Name Required!!"
		elif len ( customer.last_name ) < 4 :
			error_message = "Last Name must be 4 char!!"
		# phone number validation
		elif not customer.phone :
			error_message = "Phone number must Required!!"
		elif len ( customer.phone ) < 9 :
			error_message = "Phone Number must be 10 char!!"
		# password validation
		elif len ( customer.password ) < 6 :
			error_message = "Password must be 6 char long"
		# Email validation
		elif not customer.email :
			error_message = "Email must Required!!"
		elif len ( customer.email ) < 5 :
			error_message = "Email must be 4 char!!"
		elif customer.isExists ( ) :
			error_message = "Email Address Already Exists!"
		
		return error_message
