from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('open_demo_account/', views.open_demo_account, name='open_demo_account'),
    path('open_live_account/', views.open_live_account, name='open_live_account'),
    path('getting_started/', views.getting_started, name='getting_started'),
    path('account_types/', views.account_types, name='account_types'),
    path('education/', views.education, name='education'),
    path('deposit_withdrawal/', views.deposit_withdrawal, name='deposit_withdrawal'),
    path('investment/', views.investment, name='investment'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('register/', views.register, name='register'),
    path('economic_calender/', views.Economic_calender, name='economic_calender'),
    path('platforms/', views.platforms, name='platforms'),
    path('economic_indicators/', views.ecoIndicator, name='economic_indicators')

]
handler404 = 'forex_access.views.handler404'