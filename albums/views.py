from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm
# Create your views here.


def list_albums(request):
    albums = Album.objects.all()
    # goes to database; gets all instances of the model Album
    # ^^"the Django ORM" --> a query
    return render(request, 'albums/index.html', {'albums': albums})
    # passes data to the template using the context dictionary


def add_album(request):
    if request.method == 'POST':
        new_album = AlbumForm(request.POST)
        if new_album.is_valid():
            new_album.save()
            # creating a new instance of Album
            return redirect('home')
    form = AlbumForm()
    return render(request, 'albums/add_album.html', {'form': form})


def album_info(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/album_info.html', {'album': album})


def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album_form = AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('home')
    form = AlbumForm(instance=album)
    return render(request, 'albums/edit_album.html', {'form': form})


def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect('home')
    return render(request, 'albums/delete_album.html')
