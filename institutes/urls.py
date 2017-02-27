from django.conf.urls import url
from django.contrib import admin
from verification import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^verifier_one.*', views.institute_one_verifier, name='institute_one'),
    url(r'^verifier_two.*', views.institute_two_verifier, name='institute_two'),
    url(r'^verifier_osze.*', views.institute_osze_old, name='osze_old'),
    url(r'^verifier.*', views.institute_old_verifier, name='bsi_old'),
    url(r'.*', views.institute_one_verifier, name='institute_one'),
]
