import traceback
import sys
from django.shortcuts import render
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'index.html', {})

def handler404(request, *args, **kwargs):
    return JsonResponse({'detail': 'Page not found'}, status=404)

def handler500(request, *args, **kwargs):
    logger.error(traceback.format_exc())
    return JsonResponse({'detail': 'Internal server error'}, status=500)

