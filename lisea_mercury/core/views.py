from django.views.generic import View
from django.shortcuts import render
from django.http import request
from django.http.response import HttpResponse

# core/views.py

class indexView(View):
    
    def get(self, request, *args, **kwargs):
        return render(request, 'core/index.html')

class aliveView(View):
    
    def get(self, request, *args, **kwargs):
        return HttpResponse(status=204)