from django.views.generic import ListView
from .models import Pin, Board
import json
from django.core.serializers.json import DjangoJSONEncoder



def search_result(request):
    pin = Pin.objects.all()
    qs_json = json.dumps(list(Pin.objects.values()), cls=DjangoJSONEncoder)
    return {'qs_json': qs_json, 'pin': pin}