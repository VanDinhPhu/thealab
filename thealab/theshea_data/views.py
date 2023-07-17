from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
from .models import *
import pandas as pd
import regex as re
from django.http import JsonResponse
###################################################################################################
import requests
import numpy as np


#### Import product
from theshea_data.upload.input_data.import_product import import_product
from theshea_data.upload.input_data.import_product import update_product



TOKENS = ['42c2db83-e36f-4b8c-ae92-5ff2153bbc8c']
##### Return các request


def create_csv_file(request):
	template = 'theshea_data/index.html'
	df_oders = pd.DataFrame(SapoOrder.objects.all().values(),dtype =object)
	df_oders = df_oders.rename(columns= lambda col: 'OD_' + col)
	context = {'df_oders':df_oders.to_html()}
	df_oders.to_csv(r'theshea_data/export_csv/oders.csv',index=False)

	return render(request, template, context)
@csrf_exempt
def return_json_update_database(request,func):
	template = 'theshea_data/index.html'
	context = {}
	context.update({
			'func':func,
		})
	token = request.POST.get('token','')
	TOKENS = ['42c2db83-e36f-4b8c-ae92-5ff2153bbc8c']
	if token in TOKENS:
		if request.method == "POST":

			if func == 'product_pks':
  				# order_pks = list(SapoProduct.objects.values_list("sapo_id",flat=True).order_by("sapo_id").distinct())
				variant_pks = list(SapoVariant.objects.values_list("sapo_id",flat=True))
				# order_pks = tuple(SapoOrder.objects.values_list("sapo_id",flat=True),SapoOrder.objects.values_list("status",flat=True))
				product_pks = list(SapoVariant.objects.values_list("product_id",flat=True))
				context['variant_pks'] = variant_pks
				context['product_pks'] = product_pks

	return JsonResponse(context, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def json_api_data(request,data_for):
	context = {}
	context.update({
			'data_for':data_for.lower(),
		})
	token = request.headers['token']
	func = request.headers['func']
	context.update({
			'token':token,
			'func':func,
		})

	if request.method == "POST" and token in TOKENS:

		if data_for.lower() == 'sapo-products':
			if func == 'READ':
				pass
			elif func == 'CREATE':
				for item_product in json.loads(request.body):
					import_product(item_product)

			elif func == 'UPDATE':
				for item_product in json.loads(request.body):
					update_product(item_product)
			elif func == 'DELETE':
				pass

		else:
			pass
		return JsonResponse(context, safe=False, json_dumps_params={'ensure_ascii': False})


def index(request):
		context = {'title': 'test_funtion'}
		print('123')
		return render(request, 'theshea_data/index.html', context=context)

