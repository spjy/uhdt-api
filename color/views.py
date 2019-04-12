from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Metadata
import json
from simple_rest_client.api import API
import openCVcolor1

@csrf_exempt
def index(request):
  if request.method == 'POST':

    color = openCVcolor1()
    
    return HttpResponse("Updated")
