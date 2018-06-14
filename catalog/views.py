from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.contrib.auth import login, authenticate
from catalog.forms import RegistrationForm, UserForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from .models import (
                        Song, 
                        Artist, 
                        Genre, 
                        SongInstance, 
                        UserProfile, 
                        Post, 
                        PointOfInterest, 
                        Video, 
                    )

from django.db import transaction
from django.contrib.auth import update_session_auth_hash
#import generic views for templates
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse_lazy
#Post Imports
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import (
    CreateView,
    DeleteView,
    TemplateView,
    UpdateView,
    ListView,
    DetailView,
)



# Create your views here.



@login_required
def index(request):
    '''
    View function for home page
    '''
    #Generate Count if some main objects
    num_songs = Song.objects.all().count()
    num_instances = SongInstance.objects.all().count()
    num_artist = Artist.objects.count()
    #Get number of visitors to this page
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    #Render HTML Template(Django automatically looks in templates folder!!)
    return render(request, 'index.html', context={'num_songs':num_songs, 'num_instances':num_instances, 'num_artist':num_artist, 'num_visits':num_visits})

class SongListView(generic.ListView):
    model = Song
    context_object_name = 'my_song_list' # your own name for the list as a template variable
    queryset = Song.objects.all() # Get 5 books conating the word 'war'
    template_name = 'songs/song_list.html' #specify your own template name/location


class SongDetailView(generic.DetailView):
    model = Song
    paginate_by = 10


class ArtistListView(generic.ListView):
    model = Artist
    context_object_name = 'artist_list'
    queryset = Artist.objects.all()
    template_name = 'artists/artist_list.html'

class ArtistDetailView(generic.DetailView):
    model = Artist
    paginate_by = 10

class SignUp(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class ArtistCreate(CreateView):
    model = Artist
    fields = '__all__'

class ArtistUpdate(UpdateView):
    model = Artist
    fields = ['first_name', 'stage_name']

class ArtistDelete(DeleteView):
    model = Artist
    success_url = reverse_lazy('artists')

class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('profile')

class VideoListView(ListView):
    model = Video
    paginate_by = 10


class VideoDetailView(DetailView):
    model = Video




@login_required
def profile(request):

    num_songs = Song.objects.all().count()
    num_instances = SongInstance.objects.all().count()
    num_artist = Artist.objects.count()

    message = Post.objects.all()


    return render(request, 'profile.html', context={'num_songs':num_songs, 'num_instances':num_instances, 'num_artist':num_artist, 'message':message})

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
    return render(request, 'update_profile.html', {'user_form':user_form})


@login_required
def artist_update(request):
    return render(request, 'catalog/artist_form.html')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('update_profile')
        else:
            return redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'change_password.html', {'form':form})

@login_required
def gigs(request):
    pois = PointOfInterest.objects.all()
    return render(request, 'catalog/gigs.html', {'pois':pois})



