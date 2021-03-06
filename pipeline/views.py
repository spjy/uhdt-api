from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Metadata
import json
import os
from PIL import Image
from simple_rest_client.api import API

@csrf_exempt
def index(request):
  if request.method == 'POST':
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    Metadata.objects.create(
      image_name = body['image_name'],
      image_path = body['image_path'],
      object = body['object']
      # alphanumeric = body['alphanumeric'],
      # alphanumeric_color = body['alphanumeric_color'],
      # shape_color = body['shape_color'],
    )

    # resize to 299x299 image, send off to color and alpha!!

    print('RESIZING IMAGE: ' + body['image_name'])

    os.system(f'magick mogrify -resize 299!x299! C:\watcher_directory\output\{body["image_name"]}')

    api = API(
        api_root_url='http://localhost:8000',
        json_encode_body=True,
        append_slash=True,
    )

    api.add_resource(resource_name='alphanumeric')
    api.alphanumeric.create(
      body = {
          'image_name': body['image_name'],
          'image_path': body['image_path']
      }
    )

    api.add_resource(resource_name='color')
    api.color.create(
      body = {
          'image_name': body['image_name'],
          'image_path': body['image_path']
      }
    )
    
    return HttpResponse("Written")

def alphanumeric(request):
  if request.method == 'PATCH':
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    Metadata.objects.get(image_name=body['image_name']).update(alphanumeric=body['alphanumeric'])

    return HttpResponse("Updated")

def shape_color(request):
  if request.method == 'PATCH':
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    Metadata.objects.get(image_name=body['image_name']).update(alphanumeric=body['shape_color'])

    return HttpResponse("Updated")

def alphanumeric_color(request):
  if request.method == 'PATCH':
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    Metadata.objects.get(image_name=body['image_name']).update(alphanumeric=body['alphanumeric_color'])

    return HttpResponse("Updated")

def object(request):
  if request.method == 'PATCH':
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    Metadata.objects.get(image_name=body['image_name']).update(alphanumeric=body['object'])

    return HttpResponse("Updated")
