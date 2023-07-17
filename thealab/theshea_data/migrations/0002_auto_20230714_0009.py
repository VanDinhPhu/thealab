# Generated by Django 3.0 on 2023-07-13 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theshea_data', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.RemoveField(
            model_name='fulfillmentsbillingaddress',
            name='sapofulfillment',
        ),
        migrations.DeleteModel(
            name='InventoriesTransaction',
        ),
        migrations.RemoveField(
            model_name='orderlineitemsdiscountitem',
            name='sapoorderlineitem',
        ),
        migrations.RemoveField(
            model_name='orderreturnexchangelineitem',
            name='sapoorderreturnexchange',
        ),
        migrations.RemoveField(
            model_name='orderreturnsbillingaddress',
            name='sapoorderreturn',
        ),
        migrations.RemoveField(
            model_name='ordersbillingaddress',
            name='sapoorder',
        ),
        migrations.RemoveField(
            model_name='ordersshippingaddress',
            name='sapoorder',
        ),
        migrations.RemoveField(
            model_name='purchaseordersbillingaddress',
            name='sapopurchaseorder',
        ),
        migrations.RemoveField(
            model_name='purchaseorderslineitem',
            name='sapopurchaseorder',
        ),
        migrations.RemoveField(
            model_name='purchaseordersrefund',
            name='sapopurchaseorder',
        ),
        migrations.RemoveField(
            model_name='receiptslineitem',
            name='saporeceipts',
        ),
        migrations.RemoveField(
            model_name='receiptslineitemlineitem',
            name='receiptslineitem',
        ),
        migrations.RemoveField(
            model_name='refundlineitemslineitem',
            name='saporefundlineitems',
        ),
        migrations.DeleteModel(
            name='Sapo_log',
        ),
        migrations.RemoveField(
            model_name='sapoaddress',
            name='sapocustomerdata',
        ),
        migrations.RemoveField(
            model_name='sapocompositeitemdomain',
            name='sapoorderlineitem',
        ),
        migrations.RemoveField(
            model_name='sapocustomerdata',
            name='sapoorder',
        ),
        migrations.RemoveField(
            model_name='sapocustomergroup',
            name='sapocustomerdata',
        ),
        migrations.RemoveField(
            model_name='sapodeliveryfee',
            name='sapoorder',
        ),
        migrations.RemoveField(
            model_name='sapodiscountitem',
            name='sapoorder',
        ),
        migrations.RemoveField(
            model_name='sapofulfillment',
            name='sapoorder',
        ),
        migrations.RemoveField(
            model_name='sapofulfillmentlineitem',
            name='sapofulfillments',
        ),
        migrations.RemoveField(
            model_name='sapoloyaltycustomer',
            name='sapocustomerdata',
        ),
        migrations.RemoveField(
            model_name='saponote',
            name='sapocustomerdata',
        ),
        migrations.RemoveField(
            model_name='sapoordercouponcode',
            name='sapoorder',
        ),
        migrations.RemoveField(
            model_name='sapoorderlineitem',
            name='sapoorder',
        ),
        migrations.RemoveField(
            model_name='sapoorderreturn',
            name='sapoorder',
        ),
        migrations.RemoveField(
            model_name='sapoorderreturnexchange',
            name='sapoorder',
        ),
        migrations.RemoveField(
            model_name='sapoorderreturnslineitem',
            name='sapoorderreturn',
        ),
        migrations.RemoveField(
            model_name='sapopayment',
            name='sapofulfillment',
        ),
        migrations.RemoveField(
            model_name='sapoprepayment',
            name='sapoorder',
        ),
        migrations.RemoveField(
            model_name='sapopromotionredemption',
            name='sapoorder',
        ),
        migrations.RemoveField(
            model_name='saporeceipt',
            name='sapopurchaseorder',
        ),
        migrations.RemoveField(
            model_name='saporefund',
            name='sapoorderreturn',
        ),
        migrations.RemoveField(
            model_name='saporefundlineitem',
            name='purchaseordersrefund',
        ),
        migrations.RemoveField(
            model_name='saposaleorder',
            name='sapocustomerdata',
        ),
        migrations.RemoveField(
            model_name='saposhipment',
            name='sapofulfillment',
        ),
        migrations.RemoveField(
            model_name='saposupplieraddress',
            name='sapopurchaseorder',
        ),
        migrations.RemoveField(
            model_name='shipmentshippingaddress',
            name='saposhipment',
        ),
        migrations.DeleteModel(
            name='StockAdjustment',
        ),
        migrations.DeleteModel(
            name='StockAdjustmentLine',
        ),
        migrations.DeleteModel(
            name='FulfillmentsBillingAddress',
        ),
        migrations.DeleteModel(
            name='OrderLineItemsDiscountItem',
        ),
        migrations.DeleteModel(
            name='OrderReturnExchangeLineItem',
        ),
        migrations.DeleteModel(
            name='OrderReturnsBillingAddress',
        ),
        migrations.DeleteModel(
            name='OrdersBillingAddress',
        ),
        migrations.DeleteModel(
            name='OrdersShippingAddress',
        ),
        migrations.DeleteModel(
            name='PurchaseOrdersBillingAddress',
        ),
        migrations.DeleteModel(
            name='PurchaseOrdersLineItem',
        ),
        migrations.DeleteModel(
            name='PurchaseOrdersRefund',
        ),
        migrations.DeleteModel(
            name='ReceiptsLineItem',
        ),
        migrations.DeleteModel(
            name='ReceiptsLineItemLineItem',
        ),
        migrations.DeleteModel(
            name='RefundLineItemsLineItem',
        ),
        migrations.DeleteModel(
            name='SapoAddress',
        ),
        migrations.DeleteModel(
            name='SapoCompositeItemDomain',
        ),
        migrations.DeleteModel(
            name='SapoCustomerData',
        ),
        migrations.DeleteModel(
            name='SapoCustomerGroup',
        ),
        migrations.DeleteModel(
            name='SapoDeliveryFee',
        ),
        migrations.DeleteModel(
            name='SapoDiscountItem',
        ),
        migrations.DeleteModel(
            name='SapoFulfillment',
        ),
        migrations.DeleteModel(
            name='SapoFulfillmentLineItem',
        ),
        migrations.DeleteModel(
            name='SapoLoyaltyCustomer',
        ),
        migrations.DeleteModel(
            name='SapoNote',
        ),
        migrations.DeleteModel(
            name='SapoOrder',
        ),
        migrations.DeleteModel(
            name='SapoOrderCouponCode',
        ),
        migrations.DeleteModel(
            name='SapoOrderLineItem',
        ),
        migrations.DeleteModel(
            name='SapoOrderReturn',
        ),
        migrations.DeleteModel(
            name='SapoOrderReturnExchange',
        ),
        migrations.DeleteModel(
            name='SapoOrderReturnsLineItem',
        ),
        migrations.DeleteModel(
            name='SapoPayment',
        ),
        migrations.DeleteModel(
            name='SapoPrepayment',
        ),
        migrations.DeleteModel(
            name='SapoPromotionRedemption',
        ),
        migrations.DeleteModel(
            name='SapoPurchaseOrder',
        ),
        migrations.DeleteModel(
            name='SapoReceipt',
        ),
        migrations.DeleteModel(
            name='SapoRefund',
        ),
        migrations.DeleteModel(
            name='SapoRefundLineItem',
        ),
        migrations.DeleteModel(
            name='SapoSaleOrder',
        ),
        migrations.DeleteModel(
            name='SapoShipment',
        ),
        migrations.DeleteModel(
            name='SapoSupplierAddress',
        ),
        migrations.DeleteModel(
            name='ShipmentShippingAddress',
        ),
    ]