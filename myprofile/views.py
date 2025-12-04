from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import User
from .forms import SignupForm, LoginForm
from django.contrib.auth.hashers import make_password, check_password
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.conf import settings


def login_required(view_func):
    @never_cache
    def wrapper(request, *args, **kwargs):
        if not request.session.get('user_id'):
            from django.contrib import messages
            messages.warning(request, 'ログインしてください')
            return redirect(f"{settings.LOGIN_URL}?next={request.path}")
        return view_func(request, *args, **kwargs)
    return wrapper

# 新規登録
class SignupView(View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(user.password)
            user.save()
            # セッションにユーザーIDを保存してログイン状態に
            request.session['user_id'] = str(user.id)
            return redirect('myprofile:index')
        return render(request, 'registration/signup.html', {'form': form})

# ログイン
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'registration/login.html', {'form': form})
        
        name = form.cleaned_data['name']
        password = form.cleaned_data['password']

        try:
            user = User.objects.get(name=name)
            if check_password(password, user.password):
                request.session['user_id'] = str(user.id)
                return redirect('myprofile:index')
            else:
                messages.error(request, 'パスワードが間違っています')
        except User.DoesNotExist:
            messages.error(request, 'その名前は登録されていません')
        return render(request, 'registration/login.html', {'form': form})
# ログアウト
class LogoutView(View):
    def get(self, request):
        return render(request, 'registration/logout.html')
    
    def post(self, request):
        request.session.flush()
        return redirect('myprofile:index')
    
class IndexView(View):
    def get(self, request):
        return render(request, 'myprofile/index.html')
    
@method_decorator(login_required, name="dispatch")
class HistoryView(View):
    def get(self, request):
        return render(request, 'myprofile/history.html')
    
@method_decorator(login_required, name="dispatch")
class GamePlayView(View):
    def get(self, request):
        return render(request, 'myprofile/game-play.html')
