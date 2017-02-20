from django.conf.urls import url
from django.contrib import admin
from verification import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^verifier', views.institute_old_verifier, name='institute_old'),
    url(r'^verifier_one', views.institute_one_verifier, name='institute_one'),
    url(r'.*', views.institute_old_verifier, name='institute_old'),
]
