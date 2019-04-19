from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pipeline.models import Metadata
import json
from simple_rest_client.api import API
from .openCVcolor1 import main

@csrf_exempt
def index(request):
  if request.method == 'POST':

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    color = main(body['image_path'])

    Metadata.objects.get(image_name=body['image_name']).update(alphanumeric_color=color.alphanumeric_color)
    Metadata.objects.get(image_name=body['image_name']).update(shape_color=color.shape_color)

    return HttpResponse("Updated")
