from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
  if request.method == 'POST':
    return HttpResponse("Hello, world.")
