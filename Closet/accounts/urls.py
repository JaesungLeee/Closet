from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup), #회원가입
    path('login/', login), # 로그인
    path('kakao_login/', kakao_login), # kakao login
    path('google_login/', google_login), # google login
    path('activate/<str:uidb64>/<str:token>', Activate.as_view()), # email 인증
    path('email-verify/', email_verify),
    path('clothes_info/', ClothesInfo.as_view()), # 옷 정보 받기, IN/OUT check
    path('clothes_list/', ClothesList.as_view()),
    # path('recommendation'), # 옷 추천 리스트
]