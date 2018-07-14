from django.conf.urls import include, url


urlpatterns = [
    url(r'^hello/', include('hello.urls', namespace='hello')),
    url(r'^crud/', include('crud.urls', namespace='crud')),
    url(r'^guestboard/', include('guestboard.urls', namespace='guestboard')),  # 追加する
]
