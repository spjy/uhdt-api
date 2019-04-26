from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pipeline.models import Metadata
import json
from .getValues import main
# from .label_image import main
from simple_rest_client.api import API

@csrf_exempt
def index(request):
  if request.method == 'POST':

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    Metadata.objects.get(image_name=body['image_name']).update(object=body)

    api = API(
        api_root_url='http://localhost:8000',
        json_encode_body=True,
        append_slash=True,
    )

    api.add_resource(resource_name='alphanumeric')
    api.object.create(
      body = {
          'image_name': body['image_name'],
          'image_path': body['image_path']
      }
    )

    api.add_resource(resource_name='color')
    api.object.create(
      body = {
          'image_name': body['image_name'],
          'image_path': body['image_path']
      }
    )

    return HttpResponse("Hello, world.")
