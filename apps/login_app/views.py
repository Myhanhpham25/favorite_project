# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from models import User
import re
import bcrypt

def index(request):
	
	return render(request, 'login_app/index.html')

def register(request):
	results = User.objects.validate(request.POST)
	if results['status'] == False:
		for error in results['errors']:
			messages.error(request, error)
		return redirect("/")
	else:
		user = User.objects.create(
			name = request.POST['name'], 
			alias = request.POST['alias'], 
			email = request.POST['email'],
			password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()),
			birthday = request.POST['birthday']
			)
		messages.success(request, "Sucessfully registered! Please login now!")
		return redirect("/")

def login(request):
	print request.POST
	results = User.objects.loginVal(request.POST)


	if results['status'] == False:
		messages.error(request, "Please check your email and password and try again")
		return redirect('/')
	else:
		request.session['email'] = results['users'].email
		request.session['name'] = results['users'].name
		request.session['id'] = results['users'].id
		return redirect('/favorite')

def logout(request):
	request.session.flush()

	return redirect("/")

	





