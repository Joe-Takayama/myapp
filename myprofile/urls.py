from django.urls import path
from .views import IndexView, HistoryView, GamePlayView, SignupView, LoginView, LogoutView

app_name = 'myprofile'
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('history/', HistoryView.as_view(), name="history"),
    path('game-play/', GamePlayView.as_view(), name='game-play'),
    path('signup/', SignupView.as_view(), name="signup"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
