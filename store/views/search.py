from django.views import View
from django.shortcuts import render,redirect
from .index import Index

class Search(View):
    def get(self, request):
        query = request.GET.get('search')
        price = request.GET.get('price')
        return render(request,'search.html',Index.dict(request, query, price))