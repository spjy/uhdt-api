from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .label_image import main

@csrf_exempt
def index(request):
  if request.method == 'POST':

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    alphanumeric = main(body['image_path'])

    Metadata.objects.get(image_name=body['image_name']).update(alphanumeric=alphanumeric)

    return HttpResponse("Hello, world.")
