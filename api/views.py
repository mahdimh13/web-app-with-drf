from django.shortcuts import render,redirect,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item , History
from . import serlializers
from rest_framework import serializers
from rest_framework import status


# urls help
#    
#         'all_items': '/all',
#         'Search by key': '/?key=key_name',
#         
#         'Add': '/create',
#         'Update': '/update/pk',
#         'history:'/history/?key=key_name'    
# 

@api_view(['POST'])
def add_items(request):
	item = serlializers.ItemSerializer(data=request.data)

	# validating for already existing data
	if Item.objects.filter(**request.data).exists():
		raise serializers.ValidationError('This data already exists')



	if item.is_valid():
		item.save()
		return Response(item.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)






@api_view(['GET'])
def view_items(request):
    # checking for the parameters from the URL

    if request.query_params:
        key=request.query_params.get("key")
        value=request.query_params.get("value")
        if key:
            items = Item.objects.filter(key=key)
        if value:
            items = Item.objects.filter(value=value)
    else:
        items = Item.objects.all()

    # if there is something in items else raise error
    if items:
        data = serlializers.ItemSerializer(items, many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_items(request, pk):
    item = Item.objects.get(pk=pk)


    print("item is:",item)
    data = serlializers.ItemSerializer(instance=item,data=request.data   )

    data.is_valid()
    if data.validated_data.get("value")!=item.value:

        History.objects.create(key=item.key, value=item.value)


    if data.validated_data.get("key")==pk:


        data.save()


        return Response(data.data)
        
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def history(request):
    # checking for the parameters from the URL
    if request.query_params:
        key=request.query_params.get("key")
        if key:
            items = History.objects.filter(key=key)
    if items:
        data = serlializers.HistorySerializer(items, many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)