from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pipeline.models import Metadata
import json
from simple_rest_client.api import API
from .openCVcolor1 import main
import os

@csrf_exempt
def index(request):
  if request.method == 'POST':

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    color = main(body['image_path'] + os.sep + body['image_name'])

    print(color)

    metadata = Metadata.objects.get(image_name=body['image_name'])

    if color['shape_color']:
      metadata.shape_color = color['shape_color']
      
    if color['alphanumeric_color']:
      metadata.alphanumeric_color = color['alphanumeric_color']

    metadata.save()

    return HttpResponse("Updated")
