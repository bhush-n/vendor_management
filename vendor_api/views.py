# vendor_api/views.py
from datetime import timezone
from rest_framework import generics
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer
from django.shortcuts import render
from .models import Vendor


def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request, 'vendor_list.html', {'vendors': vendors})


class VendorListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class PurchaseOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class VendorPerformanceView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class PurchaseOrderAcknowledgmentView(generics.UpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def perform_update(self, serializer):
        serializer.save(acknowledgment_date=timezone.now())


class VendorHistoricalPerformanceView(generics.ListCreateAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
    # ... rest of the class ...
