from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from common.forms import UserForm

from Ryugiohproject_app.models import Card
from .models import LikeList
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

import json



# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            # login(request, user)  # 로그인
            return redirect('login')
        else:
            # 폼이 유효하지 않은 경우 signup 변수를 True로 설정
            return redirect(f"{request.path}?signup=true")
    else:
        form = UserForm()

    return render(request, 'common/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')

# def like_toggle(request):
#     user = request.user
#     card_id = request.GET.get('card_id', 4031928)
#     card = Card.objects.get(id=card_id)

#     if not LikeList.objects.filter(user=user, card=card).exists():
#         LikeList(user=user, card=card).save()
#         result = 'like'
#     else:
#         LikeList.objects.filter(user=user, card=card).delete()
#         result = 'unlike'

#     return render(request, 'common/like.html')

@csrf_exempt
def like_toggle(request):
    data = json.loads(request.body)
    card_id = data.get('card_id')

    if request.method == 'POST':
        user = request.user
        card = get_object_or_404(Card, id=card_id)

        try:
            like = LikeList.objects.get(user=user, card=card)
            like.delete()
            result = 'unlike'
        except LikeList.DoesNotExist:
            LikeList.objects.create(user=user, card=card)
            result = 'like'

        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': card_id}, status=400)

def like_status(request, card_id):
    user = request.user
    card = get_object_or_404(Card, id=card_id)
    liked = LikeList.objects.filter(user=user, card=card).exists()
    return JsonResponse({'liked': liked})

def mypage(request):
    user = request.user
    like_list = LikeList.objects.filter(user=user).select_related('card')
    info = {
        'username' : user.username,
        'name': user.first_name,
        'email': user.email,
        'like_list': like_list,
    }
    
    return render(request, 'common/my_page.html', {'info': info})