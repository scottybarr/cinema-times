from django.http import HttpResponse
from django.utils import simplejson


def home(request):
    data = simplejson.dumps({'cinemas': []})
    return HttpResponse(data, mimetype='application/json')
