from django.shortcuts import render
from .models import obituary_platform
from .forms import ObituaryForm



def obituary_form(request):
	if request.method == 'POST':
		form = ObituaryForm(request.POST or None)
		if form.is_valid():
			form.save()
		return render(request, 'home.html', {})

	else:
		return render(request, 'obituary_form.html',{})




def home(request):
	all_obituaries = obituary_platform.objects.all
	return render(request, 'home.html',{'all':all_obituaries})