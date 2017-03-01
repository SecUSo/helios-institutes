from django.conf.urls import url
from django.contrib import admin
from verification import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^verifier_one.*', views.institute_one_verifier, name='institute_oneDE'),
    url(r'^verifier_two.*', views.institute_two_verifier, name='institute_twoDE'),
    url(r'^verifier_osze.*', views.institute_osze_old, name='osze_oldDE'),
    url(r'^verifier.*', views.institute_old_verifier, name='bsi_oldDE'),
    url(r'.*', views.institute_one_verifier, name='institute_oneDE'),
]
