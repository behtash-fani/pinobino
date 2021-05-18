from django.urls import path
from . import views



app_name = 'accounts'
urlpatterns = [
    path('singup/', views.UserRegister.as_view(), name='register'),
    path('singin/', views.UserLogin.as_view(), name='login'),
    path('singout/', views.UserLogout.as_view(), name='logout'),
    path('profile/<str:username>', views.UserDashboard.as_view(), name='dashboard'),
    path('dashboard/<str:username>/update/', views.UpdateUserProfile.as_view(), name='update_profile'),
    path('dashboard/<str:username>/pins', views.UserPins.as_view(), name='user_pins'),
    path('dashboard/pin/delete/<str:id>', views.DeletePinView.as_view(), name='delete_pin'),
    path('dashboard/<str:username>/newpin/', views.NewPinView.as_view(), name='new_pin'),
    path('dashboard/<str:username>/boards', views.UserBoards.as_view(), name='user_boards'),
    path('dashboard/<str:username>/newboard/', views.CreateBoardView.as_view(), name='newboard'),
    path('dashboard/photo/remove/' , views.RemovePhotoView.as_view(), name='remove_photo'),
    path('follow/', views.FollowView.as_view(), name='follow'),
    path('unfollow/', views.UnfollowView.as_view(), name='unfollow'),
    path('quicksave/<str:id>', views.QuickSaveView.as_view(), name='quicksave'),
    path('quicksave/remove/<str:id>', views.RemoveQuickSaveView.as_view(), name='remove_quicksave'),
    path('addtoboard/<str:pinid>/<str:boardid>', views.AddPinToBoard.as_view(), name='addtoboard'),
    
]
