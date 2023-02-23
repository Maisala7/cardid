from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from cardapp import views as v1
from rest_framework.authtoken import views as v2
from rest_framework.authtoken.views import obtain_auth_token
#router = DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', v1.register),
    path('get_user_info/', v1.get_user_info),
    path('card_info/', v1.card_info),
    path('Payment_info/', v1.Payment_infos),
    path('Payment_confirmation/', v1.Payment_confirmation),
    path('get_user_request/', v1.get_user_request),
    path('get_user_datails/', v1.get_user_datails), 
    path('show_my_report/', v1.show_my_report),
    path('date/', v1.notification_date),
    path('anthing/', v1.anything),
    path('accept_card/', v1.accept_card),
    path('reject_card/', v1.reject_card),


    #path('token/', obtain_auth_token),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', v2.obtain_auth_token),
    #path('get_my_info/', v1.get_my_info),
  #  path('cbv/<int:pk>', v1.CBV_pk.as_view()),
   # path('CBV_List', v1.CBV_List.as_view()),
    #path('CBV_user/', v1.CBV_List_user.as_view()),
    #path('CBV_user/<int:pk>', v1.CBV_user.as_view()),
    #path("get-details",views.UserDetailAPI),
]
