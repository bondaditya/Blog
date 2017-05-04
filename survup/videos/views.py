import random 
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ( CreateView, DetailView, ListView, UpdateView, DeleteView)

from .models import Video 
from .forms import VideoForm
from .mixin import MemberRequiredMixin, StaffMemberRequiredMixin

class VideoCreateView(StaffMemberRequiredMixin, CreateView):
	model = Video
	form_class = VideoForm

class VideoDetailView(MemberRequiredMixin, DetailView):
	queryset = Video.objects.all()

	#def get_object(self):
	#	return get_object_or_404(Video, slug=self.kwargs.get("abc"))

	def get_context_data(self, id=None,  *args, **kwargs):
		context = super(VideoDetailView, self).get_context_data(*args, **kwargs)
		print(context)
		return context 

class VideoListView(ListView):
	

	 def get_queryset(self):
	        request = self.request
	        qs = Video.objects.all()
	        query=request.GET.get('q')
	        if query:
	            qs = qs.filter(title__icontains=query)
	        return Video.objects.all()  #.filter(title__icontains='vid') #.filter(user=self.request.user)

	
class VideoUpdateView(StaffMemberRequiredMixin, UpdateView):
    queryset = Video.objects.all()
    form_class = VideoForm


class VideoDeleteView(StaffMemberRequiredMixin, DeleteView):
    queryset = Video.objects.all()
    success_url = '/videos/'

