from django.db import models
from django.core.serializers.json import DjangoJSONEncoder
import json


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=20, unique=True)
    on_time_delivery_rate = models.FloatField(null=True, blank=True)
    quality_rating_avg = models.FloatField(null=True, blank=True)
    average_response_time = models.FloatField(null=True, blank=True)
    fulfillment_rate = models.FloatField(null=True, blank=True)


class PurchaseOrder(models.Model):
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, related_name='purchase_orders')
    po_number = models.CharField(max_length=20, unique=True)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField(null=True, blank=True)
    items = models.CharField(max_length=1000)  # Adjust max_length as needed
    quantity = models.IntegerField()
    status = models.CharField(max_length=20)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def set_items(self, items):
        # Convert Python object to JSON string before saving to the database
        self.items = json.dumps(items, cls=DjangoJSONEncoder)

    def get_items(self):
        # Convert JSON string to Python object when retrieving from the database
        return json.loads(self.items)

    items_json = property(get_items, set_items)


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
