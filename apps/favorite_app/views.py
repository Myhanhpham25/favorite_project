# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..login_app.models import User
from models import Quote
import re
from django.contrib import messages



def dashboard(request):
	
	curUser = User.objects.get(id = request.session['id'])
	quotes= Quote.objects.all()
	
	context = {

		'user' : User.objects.get(id = request.session['id']),
		'others' : User.objects.exclude(id= request.session['id']),
		'quotes' : Quote.objects.all(),
		'myfavorite' :[],
		'allquotes' : []

		}
		
	for quote in quotes:
		if quote not in curUser.quotes.all():
			context['myfavorite'].append(quote)
		if quote in curUser.quotes.all():
			context['allquotes'].append(quote)


	return render(request, 'favorite_app/dashboard.html', context)

def add(request):


	results = Quote.objects.quoteVal(request.POST)

	if results['status'] == False:
		for error in results['errors']:
			messages.error(request, error)
		return redirect("/favorite")
	else:
		quote = Quote.objects.creator(request.POST)
	print quote

	user = User.objects.get(id= request.session['id'])
	print user

	Quote.objects.relate(quote, user)

	return redirect('/favorite')

def addfavorite(request, id):

	quote = Quote.objects.get(id = id)
	user = User.objects.get(id = request.session['id'])
	Quote.objects.relate(quote, user)

	return redirect('/favorite')

def remove(request, id):

	quote = Quote.objects.get(id = id )
	user = User.objects.get( id = request.session['id'])
	user.quotes.remove(quote)

	return redirect('/favorite')

def show(request, id):

	context = {

	'user' : User.objects.get(id = id)

	}

	return render(request, 'favorite_app/show.html', context)

 