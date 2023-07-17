from django.db import models


# SapoProducts
class SapoProduct(models.Model):
    sapo_id = models.TextField(null=True, blank=True)
    tenant_id = models.TextField(null=True, blank=True)
    created_on = models.TextField(null=True, blank=True)
    modified_on = models.TextField(null=True, blank=True)
    status = models.TextField(null=True, blank=True)
    brand = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image_path = models.TextField(null=True, blank=True)
    image_name = models.TextField(null=True, blank=True)
    name = models.TextField(null=True, blank=True)
    opt1 = models.TextField(null=True, blank=True)
    opt2 = models.TextField(null=True, blank=True)
    opt3 = models.TextField(null=True, blank=True)
    category_id = models.TextField(null=True, blank=True)
    category = models.TextField(null=True, blank=True)
    category_code = models.TextField(null=True, blank=True)
    tags = models.TextField(null=True, blank=True)
    medicine = models.TextField(null=True, blank=True)
    product_type = models.TextField(null=True, blank=True)
    product_medicines = models.TextField(null=True, blank=True)
    # variants: SapoVariants,
    # options: SapoOptions,
    # images: ProductsImage

    def __str__(self):
        return f'{self.name}'


class SapoVariant(models.Model):
    sapo_id = models.TextField(null=True, blank=True)
    tenant_id = models.TextField(null=True, blank=True)
    location_id = models.TextField(null=True, blank=True)
    created_on = models.TextField(null=True, blank=True)
    modified_on = models.TextField(null=True, blank=True)
    category_id = models.TextField(null=True, blank=True)
    brand_id = models.TextField(null=True, blank=True)
    product_id = models.TextField(null=True, blank=True)
    composite = models.TextField(null=True, blank=True)
    init_price = models.TextField(null=True, blank=True)
    init_stock = models.TextField(null=True, blank=True)
    variant_retail_price = models.TextField(null=True, blank=True)
    variant_whole_price = models.TextField(null=True, blank=True)
    variant_import_price = models.TextField(null=True, blank=True)
    image_id = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    name = models.TextField(null=True, blank=True)
    opt1 = models.TextField(null=True, blank=True)
    opt2 = models.TextField(null=True, blank=True)
    opt3 = models.TextField(null=True, blank=True)
    product_name = models.TextField(null=True, blank=True)
    product_status = models.TextField(null=True, blank=True)
    status = models.TextField(null=True, blank=True)
    sellable = models.TextField(null=True, blank=True)
    sku = models.TextField(null=True, blank=True)
    barcode = models.TextField(null=True, blank=True)
    taxable = models.TextField(null=True, blank=True)
    weight_value = models.TextField(null=True, blank=True)
    weight_unit = models.TextField(null=True, blank=True)
    unit = models.TextField(null=True, blank=True)
    packsize = models.TextField(null=True, blank=True)
    packsize_quantity = models.TextField(null=True, blank=True)
    packsize_root_id = models.TextField(null=True, blank=True)
    packsize_root_sku = models.TextField(null=True, blank=True)
    packsize_root_name = models.TextField(null=True, blank=True)
    tax_included = models.TextField(null=True, blank=True)
    input_vat_id = models.TextField(null=True, blank=True)
    output_vat_id = models.TextField(null=True, blank=True)
    input_vat_rate = models.TextField(null=True, blank=True)
    output_vat_rate = models.TextField(null=True, blank=True)
    product_type = models.TextField(null=True, blank=True)
    warranty = models.TextField(null=True, blank=True)
    warranty_term_id = models.TextField(null=True, blank=True)
    expiration_alert_time = models.TextField(null=True, blank=True)
    # variant_prices: SapoVariantPrices,
    # inventories: SapoInventories,
    # images: VariantsImages,
    # composite_items: SapoCompositeItems
    sapoproduct = models.ForeignKey(
        SapoProduct, related_name='sapoproduct_sapovariants', blank=True, null=True, on_delete=models.CASCADE)
    sku_modified = models.CharField(max_length=255, null=True, blank=True)
    # name_modified = models.TextField(max_length=255,null=True,blank=True)

    def __str__(self):
        return f'{self.name}'


class SapoVariantPrice(models.Model):
    sapo_id = models.TextField(null=True, blank=True)
    value = models.TextField(null=True, blank=True)
    included_tax_price = models.TextField(null=True, blank=True)
    name = models.TextField(null=True, blank=True)
    price_list_id = models.TextField(null=True, blank=True)
    sapovariant = models.ForeignKey(
        SapoVariant, related_name='sapovariant_sapovariantprices', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.sapo_id}'


class SapoPriceList(models.Model):
    sapo_id = models.TextField(null=True, blank=True)
    tenant_id = models.TextField(null=True, blank=True)
    created_on = models.TextField(null=True, blank=True)
    modified_on = models.TextField(null=True, blank=True)
    code = models.TextField(null=True, blank=True)
    currency_id = models.TextField(null=True, blank=True)
    name = models.TextField(null=True, blank=True)
    is_cost = models.TextField(null=True, blank=True)
    currency_symbol = models.TextField(null=True, blank=True)
    currency_iso = models.TextField(null=True, blank=True)
    status = models.TextField(null=True, blank=True)
    init = models.TextField(null=True, blank=True)
    sapovariantprice = models.ForeignKey(
        SapoVariantPrice, related_name='sapovariantprice_sapopricelists', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.sapo_id}'


class SapoInventory(models.Model):
    location_id = models.TextField(null=True, blank=True)
    variant_id = models.TextField(null=True, blank=True)
    mac = models.TextField(null=True, blank=True)
    amount = models.TextField(null=True, blank=True)
    on_hand = models.TextField(null=True, blank=True)
    available = models.TextField(null=True, blank=True)
    committed = models.TextField(null=True, blank=True)
    incoming = models.TextField(null=True, blank=True)
    onway = models.TextField(null=True, blank=True)
    min_value = models.TextField(null=True, blank=True)
    max_value = models.TextField(null=True, blank=True)
    bin_location = models.TextField(null=True, blank=True)
    wait_to_pack = models.TextField(null=True, blank=True)
    modified_on = models.TextField(null=True, blank=True)
    sapovariant = models.ForeignKey(
        SapoVariant, related_name='sapovariant_sapoinventories', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.location_id}'


class VariantsImage(models.Model):
    sapo_id = models.TextField(null=True, blank=True)
    size = models.TextField(null=True, blank=True)
    created_on = models.TextField(null=True, blank=True)
    modified_on = models.TextField(null=True, blank=True)
    path = models.TextField(null=True, blank=True)
    full_path = models.TextField(null=True, blank=True)
    file_name = models.TextField(null=True, blank=True)
    is_default = models.TextField(null=True, blank=True)
    position = models.TextField(null=True, blank=True)
    sapovariant = models.ForeignKey(
        SapoVariant, related_name='sapovariant_variantsimages', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.sapo_id}'


class SapoCompositeItem(models.Model):
    sub_product_id = models.TextField(null=True, blank=True)
    sub_variant_id = models.TextField(null=True, blank=True)
    price = models.TextField(null=True, blank=True)
    quantity = models.TextField(null=True, blank=True)
    sub_product_type = models.TextField(null=True, blank=True)
    sub_sku = models.TextField(null=True, blank=True)
    sub_name = models.TextField(null=True, blank=True)
    medicine = models.TextField(null=True, blank=True)
    sapovariant = models.ForeignKey(
        SapoVariant, related_name='sapovariant_sapocompositeitems', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.sub_product_id}'


class SapoOption(models.Model):
    sapo_id = models.TextField(null=True, blank=True)
    name = models.TextField(null=True, blank=True)
    position = models.TextField(null=True, blank=True)
    sapoproduct = models.ForeignKey(
        SapoProduct, related_name='sapoproduct_sapooptions', blank=True, null=True, on_delete=models.CASCADE)
    # values: SapoValues

    def __str__(self):
        return f'{self.sapo_id}'


class SapoValue(models.Model):
    code = models.TextField(null=True, blank=True)
    value = models.TextField(null=True, blank=True)
    sapooption = models.ForeignKey(
        SapoOption, related_name='sapooption_sapovalues', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.code}'


class ProductsImage(models.Model):
    sapo_id = models.TextField(null=True, blank=True)
    size = models.TextField(null=True, blank=True)
    created_on = models.TextField(null=True, blank=True)
    modified_on = models.TextField(null=True, blank=True)
    path = models.TextField(null=True, blank=True)
    full_path = models.TextField(null=True, blank=True)
    file_name = models.TextField(null=True, blank=True)
    position = models.TextField(null=True, blank=True)
    sapoproduct = models.ForeignKey(
        SapoProduct, related_name='sapoproduct_productsimages', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):

        return f'{self.sapo_id}'
# PurchaseOrders


