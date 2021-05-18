from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView, ListView
from django.views import View
from .models import Pin, Board, QuickSave

class PinsListView(View):
    template_name = 'pin_list.html'
    def get(self, request):
        user = request.user
        user_pin_save = []
        pins = Pin.objects.all()
        if user.is_authenticated:
            user_boards = Board.objects.filter(user=user)
        else:
            user_boards = ""
        save_pins = QuickSave.objects.all()
        for save in save_pins:
            if user in save.user.all():
                user_pin_save.append(save.pin.id)
        return render(request, self.template_name, {'pins':pins, 'user_pin_save':user_pin_save, 'user_boards':user_boards})

class PinView(DetailView):
    template_name = 'pin_detail.html'
    context_object_name = 'pin'
    queryset = Pin.objects.all()
    