from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('get_token')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_token_view(request):
    user = request.user
    refresh = RefreshToken.for_user(user)
    data = {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    return Response(data)