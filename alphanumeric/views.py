from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pipeline.models import Metadata
from .label_image import main
import os
import json

@csrf_exempt
def index(request):
  if request.method == 'POST':

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    alphanumeric = main(body['image_path'] + os.sep + body['image_name'])

    metadata = Metadata.objects.get(image_name=body['image_name'])

    metadata.alphanumeric = alphanumeric

    metadata.save()

    return HttpResponse("Hello, world.")
