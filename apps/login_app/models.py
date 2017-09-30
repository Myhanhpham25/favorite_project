# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
import datetime
from datetime import date 



class UserManager(models.Manager):

	def loginVal(self,postData):
		results = {'status': True, 'errors': [], 'users': None}
		users = self.filter(email = postData['email'])
		print users
		
		if len(users) < 1:
			results['status'] = False
		else: 
			if bcrypt.checkpw(postData['password'].encode(), users[0].password.encode()): 
				results['users'] = users[0]
			else: 
				results['status'] = False

		return results 


	def validate(self, postData):
		results = {'status' : True, 'errors' : []}

		for key in postData:
			if re.search(' ', postData[key]):
				results['errors'].append("No white space allowed")
				results['status'] = False 		

		if len(postData['name']) < 2:
			results['errors'].append("Your name needs to be at least two characters long.")
			results['status'] = False 

		if len(postData['alias']) < 2:
			results['errors'].append("Your alias needs to be at least two characters long.")
			results['status'] = False

		if not re.match("[^@]+@[^@]+\.[^@]+", postData['email']):
			results['errors'].append("Your email is invalid.")
			results['status'] = False 

		if len(postData['password']) < 8:
			results['errors'].append("Your password must be at least 8 characters long.")
			results['status'] = False

		if postData['password'] != postData['c_password']:
			results['errors'].append("Your password does not match.")
			results['status'] = False

		if len(postData['birthday']) < 1:
			results['errors'].append("Invalid birthdate")
			results['status'] = False

		if User.objects.filter(email = postData['email']).exists():
			results['errors'].append("Account already existed.")
			results['status'] = False

		return results


class User(models.Model):	
	name = models.CharField(max_length = 255)
	alias = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)
	password = models.CharField(max_length = 255)
	birthday = models.DateField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()

