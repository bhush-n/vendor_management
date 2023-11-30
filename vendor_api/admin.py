# vendor_api/admin.py
from django.contrib import admin
from .models import Vendor, PurchaseOrder, HistoricalPerformance


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact_details', 'address', 'vendor_code',
                    'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate')


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'po_number', 'vendor_reference_display', 'order_date', 'items',
                    'quantity', 'status', 'quality_rating', 'issue_date', 'acknowledgment_date', 'vendor')

    def vendor_reference_display(self, obj):
        return obj.vendor.vendor_code if obj.vendor else ''
    vendor_reference_display.short_description = 'Vendor Code'


@admin.register(HistoricalPerformance)
class HistoricalPerformance(admin.ModelAdmin):
    list_display = (
        'date',
        'on_time_delivery_rate',
        'quality_rating_avg',
        'average_response_time',
        'fulfillment_rate')
