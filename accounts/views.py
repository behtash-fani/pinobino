from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView
from .forms import UserRegistrationForm,UserLoginForm,UpdateProfileForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from .models import Profile, UsersRelation
from django.contrib.auth.mixins import LoginRequiredMixin
from pin.models import Pin, Board, QuickSave
from .forms import PinForm,BoardForm
from django.http import JsonResponse




# All User Personal Info View
class UserRegister(View):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create(username=cd['username'], email=cd['email'], password=cd['password'])
            profile = Profile(user=user)
            profile.save()
            messages.success(request, 'you singup successfully', 'info')
            return redirect('pin:listpin')
        return render(request, self.template_name, {'form':form})
            

class UserLogin(View):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you singin successfully', 'info')
                return redirect('pin:listpin')
            messages.error(request, 'username or password is wrong', 'warning')
        return render(request, self.template_name, {'form':form})

class UserLogout(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'you singout from your accounts', 'info')
        return redirect('pin:listpin')


class UserDashboard(View):
    template_name = 'accounts/dashboard.html'
    
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        userpins  = Pin.objects.filter(user=user)
        following = UsersRelation.objects.filter(from_user=user)
        followers = UsersRelation.objects.filter(to_user=user)
        self_dash = False
        is_following = False
        if request.user.is_authenticated:
            relation = UsersRelation.objects.filter(from_user=request.user, to_user=user)
            if relation.exists():
                is_following = True
        else:
            is_following = False
        
        if request.user.id == user.id:
            self_dash = True
        context = {
            'user':user,
            'userpins':userpins,
            'self_dash':self_dash,
            'is_following':is_following,
            'followers': followers,
            'following' : following,
            }
        return render(request, self.template_name, context)


class UpdateUserProfile(LoginRequiredMixin, View):
    template_name = 'accounts/update_profile.html'
    form_class = UpdateProfileForm

    def get(self, request, username):
        initial_dict = {"email" : request.user.email,"first_name" : request.user.first_name,"last_name":request.user.last_name,}
        user = get_object_or_404(User, username=username)
        form = self.form_class(instance=request.user.profile, initial = initial_dict)
        return render(request, self.template_name, {'user':user, 'form':form})
    
    def post(self, request, *args, **kwargs):
        initial_dict = {"email" : request.user.email,"first_name" : request.user.first_name,"last_name":request.user.last_name,}
        form = self.form_class(request.POST, request.FILES, instance=request.user.profile, initial = initial_dict)
        if form.is_valid():
            print(form.cleaned_data['email'])
            newform = form.save(commit=False)
            newform.user = request.user
            newform.save()
            request.user.email = form.cleaned_data['email']
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.save()
            messages.success(request, 'your personal info has been updated', 'info')
            return redirect('accounts:dashboard', request.user.username)
        return render(request, self.template_name, {'form':form})

class RemovePhotoView(LoginRequiredMixin, View):
    template_name = 'accounts/dashboard.html'
    def get(self, request):
        user = request.user
        profile = get_object_or_404(Profile, user=user)
        profile.photo.delete()
        return redirect('accounts:dashboard', request.user)

#All view that user need to send pin and create board
class UserPins(LoginRequiredMixin, View):
    template_name = 'accounts/user_pins.html'

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        userpins = Pin.objects.filter(user=user)
        return render(request, self.template_name, {'userpins':userpins})


class NewPinView(LoginRequiredMixin,View):
    template_name = 'accounts/new_pin.html'
    form_class = PinForm

    def get(self, request, username):
        form = self.form_class
        return render(request, self.template_name, {'form':form})

    def post(self, request, username=None):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.user = request.user
            newpost.slug = newpost.id
            newpost.save()
            messages.success(request, 'your new post created successfully', 'info')
            return redirect("accounts:user_pins", request.user)
        return render(request, self.template_name, {'form':form})

class DeletePinView(LoginRequiredMixin, View):
    def get(self, request, id=None):
        pin = get_object_or_404(Pin, id=id)
        if pin.user.username == request.user.username:
            pin.delete()
        else:
            messages.warning(request, 'you are not allow to delete this pin', 'info')    
        messages.success(request, 'your pin has been deleted successfully', 'info')
        return redirect("accounts:user_pins", request.user)

class UserBoards(LoginRequiredMixin, View):
    template_name = 'accounts/user_boards.html'

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        boards = Board.objects.filter(user=user).order_by('-created')
        return render(request, self.template_name, {'boards':boards})

class CreateBoardView(LoginRequiredMixin,View):
    template_name = 'accounts/new_board.html'
    form_class = BoardForm

    def get(self, request, username):
            form = self.form_class
            return render(request, self.template_name, {'form':form})

    def post(self, request, username=None):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.user = request.user
            newpost.slug = newpost.id
            newpost.save()
            messages.success(request, 'your new board created successfully', 'info')
            return redirect("accounts:user_boards", request.user.username)
        return render(request, self.template_name, {'form':form})


class BoardView(DetailView):
    template_name = 'board_detail.html'
    context_object_name = 'board'
    queryset = Board.objects.all()

#all view that required for follow and unfollow for users
class FollowView(LoginRequiredMixin, View):
    def post(self, request):
        user_id = request.POST['user_id']
        following = get_object_or_404(User, pk=user_id)
        check_relation = UsersRelation.objects.filter(from_user=request.user, to_user=following)
        if check_relation.exists():
            return JsonResponse({'status':'exists'})
        else:
            UsersRelation.objects.create(from_user=request.user, to_user=following)
            return JsonResponse({'status':'ok'})


class UnfollowView(LoginRequiredMixin, View):
    def post(self, request):
        user_id = request.POST['user_id']
        following = get_object_or_404(User, pk=user_id)
        check_relation = UsersRelation.objects.filter(from_user=request.user, to_user=following)
        if check_relation.exists():
             check_relation.delete()
             return JsonResponse({'status':'ok'})
        else:
            return JsonResponse({'status':'notexists'})

class QuickSaveView(LoginRequiredMixin, View):
    template_name = 'pin_list.html'

    def get(self, request, id=None):
        user = get_object_or_404(User, id=request.user.id)
        pin = get_object_or_404(Pin, id=id)
        quicksave_pin = QuickSave.objects.filter(pin=pin)
        if len(quicksave_pin) > 0:
            quicksave_pin[0].user.add(user)
            return redirect("pin:listpin")
        else:
            q_save = QuickSave.objects.create(pin=pin)
            q_save.user.add(user)
            q_save.save()
            return redirect("pin:listpin")
        
        return render(request, self.template_name)
    def post(self, request):
        pass

class RemoveQuickSaveView(View):
    def get(self, request, id=None):
        user = get_object_or_404(User, id=request.user.id)
        pin = get_object_or_404(Pin, id=id)
        quicksave_pin = QuickSave.objects.get(pin=pin)
        quicksave_pin.user.remove(user)
        return redirect("pin:listpin")


class AddPinToBoard(LoginRequiredMixin, View):
    def get(self, request, pinid=None , boardid=None):
        pin = get_object_or_404(Pin, id=pinid)
        board = get_object_or_404(Board, id=boardid)
        board.pin.add(pin)
        return redirect('pin:listpin')
        