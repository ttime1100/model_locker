from django.urls import path
from  . import views
from django.contrib.auth.views import login, logout, password_reset, password_reset_done

urlpatterns = [
    # create routes to different views
    path('', views.index, name='index'),
    path('songs/', views.SongListView.as_view(), name='songs'),
    path('song/<int:pk>', views.SongDetailView.as_view(), name='song-detail'),
    path('artists/', views.ArtistListView.as_view(), name='artists'),
    path('artist/<int:pk>', views.ArtistDetailView.as_view(), name='artist-detail'),
    # path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('artist/create/', views.ArtistCreate.as_view(), name='artist_create'),
    path('artist/<int:pk>/update/', views.ArtistUpdate.as_view(), name='artist_update'),
    path('artist/<int:pk>/delete/', views.ArtistDelete.as_view(), name='artist_delete'),
    path('profile/password/', views.change_password, name='change_password'),
    path('profile/password/', views.change_password, name='change_password'),
    path('post/create/', views.PostCreate.as_view(), name='post_create'),
    path('profile/gigs/', views.gigs, name='gigs'),
    path('profile/moneygame/videos/<int:pk>', views.VideoDetailView.as_view(), name='video-detail'),
    path('profile/moneygame/video/', views.VideoListView.as_view(), name='video-list'),





]
