from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import orderhistory, itemcatalog
from .itemcatalog import Menu
from .serializers import OrderSerializer, MenuSerializer


class ItemAPI(APIView):

    def get(self, request):
        query_results = itemcatalog.objects.all()
        serializer = MenuSerializer(query_results, many=True)
        return Response(serializer.data)


class LoadItemAPI(APIView):

    def get(self, request):
        for i in range(Menu.count):
            itemcatalog.objects.create(
                itemname=Menu.itemnames[i],
                itemtype=Menu.itemtypes[i],
                price=Menu.prices[i],
                image=Menu.images[i]
            )
        query_results = itemcatalog.objects.all()
        serializer = MenuSerializer(query_results, many=True)
        return Response(serializer.data)


class OrderApi(APIView):

    def get(self, request):
        query_results = orderhistory.objects.all()
        serializer = OrderSerializer(query_results, many=True)
        return Response(serializer.data)

    def post(self, request):
        for i in range(len(request.data)):
            orderhistory.objects.create(
                order_id=request.data[i].get("order_id"),
                item_id=request.data[i].get("item_id"),
                username=request.data[i].get("username"),
                datetime=request.data[i].get("datetime"),
                price=request.data[i].get("price")
            )
        return Response(request.data, status=status.HTTP_201_CREATED)
