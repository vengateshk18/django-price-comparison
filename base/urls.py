from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('home',views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('email',views.email,name="email"),
    path('login/',views.login_view,name="login"),
    path('logout',views.logout_view,name="logout"),
    path('qr',views.qr,name="qr"),
    path('receive_qr_data/', views.qr, name='receive_qr_data'),
    path('product_select',views.search,name="product_select"),
    path('select_item/<path:selected_value>/', views.select_item, name='your_item_selection'),
    #path('result',views.select_item,name="resultpage"),
]