# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_app.models import User
import re

class QuoteManager(models.Manager):
	def creator(self, postData):
		quote = self.create(quote_by = postData['quote_by'], message = postData['message'])
		return quote
	def relate(self, quote, user):
		relate = user.quotes.add(quote)
		return relate

	def quoteVal(self, postData):

		results = {'status' : True, 'errors' : []}

		for key in postData:
			if re.search('     ', postData[key]):
				results['errors'].append("No white space allowed")
				results['status'] = False 		

		if len(postData['quote_by']) < 3:
			results['errors'].append("Must be at least three characters long.")
			results['status'] = False 

		if len(postData['message']) < 10:
			results['errors'].append("message must be at least 10 characters")
			results['status'] = False
		return results



class Quote(models.Model):
	quote_by = models.CharField(max_length= 255)
	message = models.TextField()
	users = models.ManyToManyField(User, related_name ="quotes")
	objects = QuoteManager()