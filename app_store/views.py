from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app_store.models import DATABASE



def product_view_json(request):
    if request.method == "GET":
        return JsonResponse(DATABASE,
                            json_dumps_params={
                                'ensure_ascii': False,
                                'indent': 4
                            })# TODO Вернуть JsonResponse с объектом DATABASE и параметрами отступов и кодировок,
        # как в приложении app_weather



def shop_view(request):
    if request.method == "GET":
        with open('app_store/shop.html', encoding="utf-8") as f:
            data = f.read()
        return HttpResponse(data)

