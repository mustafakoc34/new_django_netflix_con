from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from appUser.models import *
from appMy.models import *
# Create your views here.

def index(request):
    context = {"title": "Anasayfa"}
    return render(request, 'index.html',context)

def browseIndex(request,id):
    context = {"title": "Netflix - Browse"}
    profil = get_object_or_404(Profil, id = id)
    videos = Video.objects.all()
    context.update({
        "profil":profil,
        "videos":videos,
        })
    return render(request, 'browse-index.html', context)

def browseIndexCategory(request,id,category):
    context = {"title": "Netflix"}
    profil = get_object_or_404(Profil, id = id)
    vid_category = Category.objects.get(title = category)
    videos_filter = Video.objects.filter(category=vid_category)
    context.update({
        "profil":profil,
        "vid_category":vid_category,
        "videos_filter":videos_filter,
        })
    return render(request, 'browse-index.html', context)

def likeIndex(request,pid,vid):
    profil = Profil.objects.get(id = pid)
    video = Video.objects.get(id = vid)
    like = LikeVideo(profil = profil, video = video)
    like.save()

    return HttpResponseRedirect("/netflix/"+pid+"/all/")
