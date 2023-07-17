import json
import csv
import glob
import os
from django.conf import settings
from time import time
from datetime import datetime
from datetime import timedelta
from django.utils import timezone
import pytz
from theshea_data.models import *
UPLOAD_FOLDER = 'theshea_data'
from django.db.models.functions import Length
### Product

def import_product(item_product):
	sapoproduct_obj, sapoproduct_created = SapoProduct.objects.get_or_create(sapo_id=item_product['id'])
	if sapoproduct_created:
		print(item_product['name'])
		sapoproduct_obj.tenant_id = item_product['tenant_id']
		sapoproduct_obj.created_on = item_product['created_on']
		sapoproduct_obj.modified_on = item_product['modified_on']
		sapoproduct_obj.status = item_product['status']
		sapoproduct_obj.brand = item_product['brand']
		sapoproduct_obj.description = item_product['description']
		sapoproduct_obj.image_path = item_product['image_path']
		sapoproduct_obj.image_name = item_product['image_name']
		sapoproduct_obj.name = item_product['name']
		sapoproduct_obj.opt1 = item_product['opt1']
		sapoproduct_obj.opt2 = item_product['opt2']
		sapoproduct_obj.opt3 = item_product['opt3']
		sapoproduct_obj.category_id = item_product['category_id'] if 'category_id' in item_product else None
		sapoproduct_obj.category = item_product['category']
		sapoproduct_obj.category_code = item_product['category_code']
		sapoproduct_obj.tags = item_product['tags']
		sapoproduct_obj.medicine = item_product['medicine']
		sapoproduct_obj.product_type = item_product['product_type']
		sapoproduct_obj.product_medicines = item_product['product_medicines']
		if item_product['variants']:
			for item_variant in item_product['variants']:
				sapovariant_obj, sapovariant_created = SapoVariant.objects.get_or_create(sapo_id=item_variant['id'],)
				if sapovariant_created:
					sapovariant_obj.tenant_id = item_variant['tenant_id']
					sapovariant_obj.location_id = item_variant['location_id']
					sapovariant_obj.created_on = item_variant['created_on']
					sapovariant_obj.modified_on = item_variant['modified_on']
					sapovariant_obj.category_id = item_variant['category_id'] if 'category_id' in item_variant else None
					sapovariant_obj.brand_id = item_variant['brand_id']
					sapovariant_obj.product_id = item_variant['product_id']
					sapovariant_obj.composite = item_variant['composite']
					sapovariant_obj.init_price = item_variant['init_price']
					sapovariant_obj.init_stock = item_variant['init_stock']
					sapovariant_obj.variant_retail_price = item_variant['variant_retail_price']
					sapovariant_obj.variant_whole_price = item_variant['variant_whole_price']
					sapovariant_obj.variant_import_price = item_variant['variant_import_price']
					sapovariant_obj.image_id = item_variant['image_id']
					sapovariant_obj.description = item_variant['description']
					sapovariant_obj.name = item_variant['name']
					sapovariant_obj.opt1 = item_variant['opt1']
					sapovariant_obj.opt2 = item_variant['opt2']
					sapovariant_obj.opt3 = item_variant['opt3']
					sapovariant_obj.product_name = item_variant['product_name']
					sapovariant_obj.product_status = item_variant['product_status']
					sapovariant_obj.status = item_variant['status']
					sapovariant_obj.sellable = item_variant['sellable']
					sapovariant_obj.sku = item_variant['sku']
					sapovariant_obj.barcode = item_variant['barcode']
					sapovariant_obj.taxable = item_variant['taxable']
					sapovariant_obj.weight_value = item_variant['weight_value']
					sapovariant_obj.weight_unit = item_variant['weight_unit']
					sapovariant_obj.unit = item_variant['unit']
					sapovariant_obj.packsize = item_variant['packsize']
					sapovariant_obj.packsize_quantity = item_variant['packsize_quantity']
					sapovariant_obj.packsize_root_id = item_variant['packsize_root_id']
					sapovariant_obj.packsize_root_sku = item_variant['packsize_root_sku']
					sapovariant_obj.packsize_root_name = item_variant['packsize_root_name']
					sapovariant_obj.tax_included = item_variant['tax_included']
					sapovariant_obj.input_vat_id = item_variant['input_vat_id']
					sapovariant_obj.output_vat_id = item_variant['output_vat_id']
					sapovariant_obj.input_vat_rate = item_variant['input_vat_rate']
					sapovariant_obj.output_vat_rate = item_variant['output_vat_rate']
					sapovariant_obj.product_type = item_variant['product_type']
					sapovariant_obj.warranty = item_variant['warranty']
					sapovariant_obj.warranty_term_id = item_variant['warranty_term_id']
					sapovariant_obj.expiration_alert_time = item_variant['expiration_alert_time']
					sapovariant_obj.sapoproduct = sapoproduct_obj

					if item_variant['variant_prices']:
						for item_variant_price in item_variant['variant_prices']:
							sapovariantprice_obj, sapovariantprice_created = SapoVariantPrice.objects.get_or_create(sapo_id=item_variant_price['id'],)
							if sapovariantprice_created:
								sapovariantprice_obj.value = item_variant_price['value']
								sapovariantprice_obj.included_tax_price = item_variant_price['included_tax_price']
								sapovariantprice_obj.name = item_variant_price['name']
								sapovariantprice_obj.price_list_id = item_variant_price['price_list_id']
								sapovariantprice_obj.sapovariants = sapovariant_obj
								item_variant_price_list = item_variant_price['price_list']
								sapopricelist_obj, sapopricelist_created = SapoPriceList.objects.get_or_create(sapo_id=item_variant_price_list['id'])
								if sapopricelist_created:
									sapopricelist_obj.tenant_id = item_variant_price_list['tenant_id']
									sapopricelist_obj.created_on = item_variant_price_list['created_on']
									sapopricelist_obj.modified_on = item_variant_price_list['modified_on']
									sapopricelist_obj.code = item_variant_price_list['code']
									sapopricelist_obj.currency_id = item_variant_price_list['currency_id']
									sapopricelist_obj.name = item_variant_price_list['name']
									sapopricelist_obj.is_cost = item_variant_price_list['is_cost']
									sapopricelist_obj.currency_symbol = item_variant_price_list['currency_symbol']
									sapopricelist_obj.currency_iso = item_variant_price_list['currency_iso']
									sapopricelist_obj.status = item_variant_price_list['status']
									sapopricelist_obj.init = item_variant_price_list['init']
									sapopricelist_obj.sapovariantprice = sapovariantprice_obj
									sapopricelist_obj.save()
								sapovariantprice_obj.save()
					if item_variant['inventories']:
						for item_inventories in item_variant['inventories']:
							sapoinventories_obj,sapoinventories_created = SapoInventory.objects.get_or_create(
							variant_id = item_inventories['variant_id'],
							)
							if sapoinventories_created:
								sapoinventories_obj.location_id = item_inventories['location_id']
								sapoinventories_obj.mac = item_inventories['mac']
								sapoinventories_obj.amount = item_inventories['amount']
								sapoinventories_obj.on_hand = item_inventories['on_hand']
								sapoinventories_obj.available = item_inventories['available']
								sapoinventories_obj.committed = item_inventories['committed']
								sapoinventories_obj.incoming = item_inventories['incoming']
								sapoinventories_obj.onway = item_inventories['onway']
								sapoinventories_obj.min_value = item_inventories['min_value']
								sapoinventories_obj.max_value = item_inventories['max_value']
								sapoinventories_obj.bin_location = item_inventories['bin_location']
								sapoinventories_obj.wait_to_pack = item_inventories['wait_to_pack']
								sapoinventories_obj.modified_on = item_inventories['modified_on']
								sapoinventories_obj.sapovariant = sapovariant_obj
								sapoinventories_obj.save()
								# print(sapoinventories_obj)
					if item_variant['images']:
						for variants_image in item_variant['images']:
							variantsimages_obj, variantsimages_created = VariantsImage.objects.get_or_create(sapo_id=variants_image['id'],)
							if variantsimages_created:
								variantsimages_obj.size = variants_image['size']
								variantsimages_obj.created_on = variants_image['created_on']
								variantsimages_obj.modified_on = variants_image['modified_on']
								variantsimages_obj.path = variants_image['path']
								variantsimages_obj.full_path = variants_image['full_path']
								variantsimages_obj.file_name = variants_image['file_name']
								variantsimages_obj.is_default = variants_image['is_default']
								variantsimages_obj.position = variants_image['position']
								variantsimages_obj.sapovariants = sapovariant_obj
								variantsimages_obj.save()
					if item_variant['composite_items']:
						for item_composite in item_variant['composite_items']:
							sapocompositeitems_obj, sapocompositeitems_created = SapoCompositeItem.objects.get_or_create(
								sub_product_id = item_composite['sub_product_id'],
								sub_variant_id = item_composite['sub_variant_id'],
								sub_sku = item_composite['sub_sku'])
							if sapocompositeitems_created:
								sapocompositeitems_obj.price = item_composite['price']
								sapocompositeitems_obj.quantity = item_composite['quantity']
								sapocompositeitems_obj.sub_product_type = item_composite['sub_product_type']
								sapocompositeitems_obj.sub_name = item_composite['sub_name']
								sapocompositeitems_obj.medicine = item_composite['medicine']
								sapocompositeitems_obj.sapovariant = sapovariant_obj
								sapocompositeitems_obj.save()
					sapovariant_obj.save()
		if item_product['options']:
			for item_options in item_product['options']:
				sapooptions_obj, sapooptions_created = SapoOption.objects.get_or_create(sapo_id=item_options['id'],)
				if sapooptions_created:
					sapooptions_obj.sapo_id = item_options['id']
					sapooptions_obj.name = item_options['name']
					sapooptions_obj.position = item_options['position']
					sapooptions_obj.sapoproduct = sapoproduct_obj
					if item_options['values']:
						for item_option_value in item_options['values']:
							sapovalues_obj, sapovalues_created = SapoValue.objects.get_or_create(sapooption = sapooptions_obj,value = item_option_value)
							if sapovalues_created:
								sapovalues_obj.value = item_option_value
								sapovalues_obj.save()
					sapooptions_obj.save()
		if item_product['images']:
			for item_images in item_product['images']:
				productsimage_obj, productsimage_created = ProductsImage.objects.get_or_create(sapo_id = item_images['id'])
				if productsimage_created:
					productsimage_obj.size = item_images['size']
					productsimage_obj.created_on = item_images['created_on']
					productsimage_obj.modified_on = item_images['modified_on']
					productsimage_obj.path = item_images['path']
					productsimage_obj.full_path = item_images['full_path']
					productsimage_obj.file_name = item_images['file_name']
					productsimage_obj.position = item_images['position']
					productsimage_obj.sapoproduct = sapoproduct_obj
					productsimage_obj.save()
		sapoproduct_obj.save()

	return
def update_product(item_product):
	sapoproduct_obj, sapoproduct_created = SapoProduct.objects.get_or_create(sapo_id=item_product['id'])
	if sapoproduct_obj:
		print(item_product['name'])
		sapoproduct_obj.tenant_id = item_product['tenant_id']
		sapoproduct_obj.created_on = item_product['created_on']
		sapoproduct_obj.modified_on = item_product['modified_on']
		sapoproduct_obj.status = item_product['status']
		sapoproduct_obj.brand = item_product['brand']
		sapoproduct_obj.description = item_product['description']
		sapoproduct_obj.image_path = item_product['image_path']
		sapoproduct_obj.image_name = item_product['image_name']
		sapoproduct_obj.name = item_product['name']
		sapoproduct_obj.opt1 = item_product['opt1']
		sapoproduct_obj.opt2 = item_product['opt2']
		sapoproduct_obj.opt3 = item_product['opt3']
		sapoproduct_obj.category_id = item_product['category_id'] if 'category_id' in item_product else None
		sapoproduct_obj.category = item_product['category']
		sapoproduct_obj.category_code = item_product['category_code']
		sapoproduct_obj.tags = item_product['tags']
		sapoproduct_obj.medicine = item_product['medicine']
		sapoproduct_obj.product_type = item_product['product_type']
		sapoproduct_obj.product_medicines = item_product['product_medicines']
		if item_product['variants']:
			for item_variant in item_product['variants']:
				sapovariant_obj, sapovariant_created = SapoVariant.objects.get_or_create(sapo_id=item_variant['id'],)
				if sapovariant_obj:
					sapovariant_obj.tenant_id = item_variant['tenant_id']
					sapovariant_obj.location_id = item_variant['location_id']
					sapovariant_obj.created_on = item_variant['created_on']
					sapovariant_obj.modified_on = item_variant['modified_on']
					sapovariant_obj.category_id = item_variant['category_id'] if 'category_id' in item_variant else None
					sapovariant_obj.brand_id = item_variant['brand_id']
					sapovariant_obj.product_id = item_variant['product_id']
					sapovariant_obj.composite = item_variant['composite']
					sapovariant_obj.init_price = item_variant['init_price']
					sapovariant_obj.init_stock = item_variant['init_stock']
					sapovariant_obj.variant_retail_price = item_variant['variant_retail_price']
					sapovariant_obj.variant_whole_price = item_variant['variant_whole_price']
					sapovariant_obj.variant_import_price = item_variant['variant_import_price']
					sapovariant_obj.image_id = item_variant['image_id']
					sapovariant_obj.description = item_variant['description']
					sapovariant_obj.name = item_variant['name']
					sapovariant_obj.opt1 = item_variant['opt1']
					sapovariant_obj.opt2 = item_variant['opt2']
					sapovariant_obj.opt3 = item_variant['opt3']
					sapovariant_obj.product_name = item_variant['product_name']
					sapovariant_obj.product_status = item_variant['product_status']
					sapovariant_obj.status = item_variant['status']
					sapovariant_obj.sellable = item_variant['sellable']
					sapovariant_obj.sku = item_variant['sku']
					sapovariant_obj.barcode = item_variant['barcode']
					sapovariant_obj.taxable = item_variant['taxable']
					sapovariant_obj.weight_value = item_variant['weight_value']
					sapovariant_obj.weight_unit = item_variant['weight_unit']
					sapovariant_obj.unit = item_variant['unit']
					sapovariant_obj.packsize = item_variant['packsize']
					sapovariant_obj.packsize_quantity = item_variant['packsize_quantity']
					sapovariant_obj.packsize_root_id = item_variant['packsize_root_id']
					sapovariant_obj.packsize_root_sku = item_variant['packsize_root_sku']
					sapovariant_obj.packsize_root_name = item_variant['packsize_root_name']
					sapovariant_obj.tax_included = item_variant['tax_included']
					sapovariant_obj.input_vat_id = item_variant['input_vat_id']
					sapovariant_obj.output_vat_id = item_variant['output_vat_id']
					sapovariant_obj.input_vat_rate = item_variant['input_vat_rate']
					sapovariant_obj.output_vat_rate = item_variant['output_vat_rate']
					sapovariant_obj.product_type = item_variant['product_type']
					sapovariant_obj.warranty = item_variant['warranty']
					sapovariant_obj.warranty_term_id = item_variant['warranty_term_id']
					sapovariant_obj.expiration_alert_time = item_variant['expiration_alert_time']
					sapovariant_obj.sapoproduct = sapoproduct_obj

					if item_variant['variant_prices']:
						for item_variant_price in item_variant['variant_prices']:
							sapovariantprice_obj, sapovariantprice_created = SapoVariantPrice.objects.get_or_create(sapo_id=item_variant_price['id'],)
							if sapovariantprice_obj:
								sapovariantprice_obj.value = item_variant_price['value']
								sapovariantprice_obj.included_tax_price = item_variant_price['included_tax_price']
								sapovariantprice_obj.name = item_variant_price['name']
								sapovariantprice_obj.price_list_id = item_variant_price['price_list_id']
								sapovariantprice_obj.sapovariants = sapovariant_obj

								item_variant_price_list = item_variant_price['price_list']
								sapopricelist_obj, sapopricelist_created = SapoPriceList.objects.get_or_create(sapo_id=item_variant_price_list['id'])
								if sapopricelist_obj:
									sapopricelist_obj.tenant_id = item_variant_price_list['tenant_id']
									sapopricelist_obj.created_on = item_variant_price_list['created_on']
									sapopricelist_obj.modified_on = item_variant_price_list['modified_on']
									sapopricelist_obj.code = item_variant_price_list['code']
									sapopricelist_obj.currency_id = item_variant_price_list['currency_id']
									sapopricelist_obj.name = item_variant_price_list['name']
									sapopricelist_obj.is_cost = item_variant_price_list['is_cost']
									sapopricelist_obj.currency_symbol = item_variant_price_list['currency_symbol']
									sapopricelist_obj.currency_iso = item_variant_price_list['currency_iso']
									sapopricelist_obj.status = item_variant_price_list['status']
									sapopricelist_obj.init = item_variant_price_list['init']
									sapopricelist_obj.sapovariantprice = sapovariantprice_obj
									sapopricelist_obj.save()
								sapovariantprice_obj.save()

					if item_variant['inventories']:
						for item_inventories in item_variant['inventories']:
							sapoinventories_obj,sapoinventories_created = SapoInventory.objects.get_or_create(
							variant_id = item_inventories['variant_id'],
							)
							if sapoinventories_obj:
								sapoinventories_obj.location_id = item_inventories['location_id']
								sapoinventories_obj.mac = item_inventories['mac']
								sapoinventories_obj.amount = item_inventories['amount']
								sapoinventories_obj.on_hand = item_inventories['on_hand']
								sapoinventories_obj.available = item_inventories['available']
								sapoinventories_obj.committed = item_inventories['committed']
								sapoinventories_obj.incoming = item_inventories['incoming']
								sapoinventories_obj.onway = item_inventories['onway']
								sapoinventories_obj.min_value = item_inventories['min_value']
								sapoinventories_obj.max_value = item_inventories['max_value']
								sapoinventories_obj.bin_location = item_inventories['bin_location']
								sapoinventories_obj.wait_to_pack = item_inventories['wait_to_pack']
								sapoinventories_obj.modified_on = item_inventories['modified_on']
								sapoinventories_obj.sapovariant = sapovariant_obj
								sapoinventories_obj.save()
								# print(sapoinventories_obj)
					if item_variant['images']:
						for variants_image in item_variant['images']:
							variantsimages_obj, variantsimages_created = VariantsImage.objects.get_or_create(sapo_id=variants_image['id'],)
							if variantsimages_obj:
								variantsimages_obj.size = variants_image['size']
								variantsimages_obj.created_on = variants_image['created_on']
								variantsimages_obj.modified_on = variants_image['modified_on']
								variantsimages_obj.path = variants_image['path']
								variantsimages_obj.full_path = variants_image['full_path']
								variantsimages_obj.file_name = variants_image['file_name']
								variantsimages_obj.is_default = variants_image['is_default']
								variantsimages_obj.position = variants_image['position']
								variantsimages_obj.sapovariants = sapovariant_obj
								variantsimages_obj.save()

					if item_variant['composite_items']:
						for item_composite in item_variant['composite_items']:
							sapocompositeitems_obj, sapocompositeitems_created = SapoCompositeItem.objects.get_or_create(
								sub_product_id = item_composite['sub_product_id'],
								sub_variant_id = item_composite['sub_variant_id'],
								sub_sku = item_composite['sub_sku'])
							if sapocompositeitems_obj:
								sapocompositeitems_obj.price = item_composite['price']
								sapocompositeitems_obj.quantity = item_composite['quantity']
								sapocompositeitems_obj.sub_product_type = item_composite['sub_product_type']
								sapocompositeitems_obj.sub_name = item_composite['sub_name']
								sapocompositeitems_obj.medicine = item_composite['medicine']
								sapocompositeitems_obj.sapovariant = sapovariant_obj
								sapocompositeitems_obj.save()
					sapovariant_obj.save()

		if item_product['options']:
			for item_options in item_product['options']:
				sapooptions_obj, sapooptions_created = SapoOption.objects.get_or_create(sapo_id=item_options['id'])
				if sapooptions_obj:
					sapooptions_obj.name = item_options['name']
					sapooptions_obj.position = item_options['position']
					sapooptions_obj.sapoproduct = sapoproduct_obj
					if item_options['values']:
						for item_option_value in item_options['values']:
							sapovalues_obj, sapovalues_created = SapoValue.objects.get_or_create(sapooption = sapooptions_obj,value = item_option_value)
							if sapovalues_obj:
								sapovalues_obj.save()
					sapooptions_obj.save()
		if item_product['images']:
			for item_images in item_product['images']:
				productsimage_obj, productsimage_created = ProductsImage.objects.get_or_create(sapo_id = item_images['id'],)
				if productsimage_created:
					productsimage_obj.size = item_images['size']
					productsimage_obj.created_on = item_images['created_on']
					productsimage_obj.modified_on = item_images['modified_on']
					productsimage_obj.path = item_images['path']
					productsimage_obj.full_path = item_images['full_path']
					productsimage_obj.file_name = item_images['file_name']
					productsimage_obj.position = item_images['position']
					productsimage_obj.sapoproduct = sapoproduct_obj
					productsimage_obj.save()
		sapoproduct_obj.save()
	return
def import_product_from_json():
	start_time = time()
	#################################################################################
	filepath = f'{UPLOAD_FOLDER}/upload/json_respone_products.json'
	json_file = os.path.join(settings.BASE_DIR, filepath)
	json_content = json.load(open(json_file, encoding='utf8'))
	item_loading = 0
	for v_page in json_content:
		if json_content[v_page]['products']:
			for item_product in json_content[v_page]['products']:
				import_product(item_product)
				item_loading += 1
	if (item_loading % 1) == 0:
		time_now = datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).strftime("%d/%m/%Y - %H:%M:%S")
		print(f'|--> {item_loading} loaded [{time_now}]')
		#################################################################################
		print("--- %s seconds ---" % (time() - start_time))
	return


#### Reset product database
def reset_db_product():
	SapoProduct.objects.all().delete()
	SapoVariantPrice.objects.all().delete()
	VariantsImage.objects.all().delete()
	return

def reimport_products():
	reset_db_product()
	import_product_from_json()
	print('Import thành công')
	return

#### Order

