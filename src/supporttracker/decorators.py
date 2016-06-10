from django.shortcuts import render, redirect

def profile_required():
	if create_profile_url = create_profile_url = settings.CREATE_PROFILE_URL

	def _dec(view_func):
		def _view(request,*args,**kwargs):
			if request.user.is_authenticated():
				if request.user.userprofile = None:
					return redirect(create_profile_url)
				else:
					return view_func(request,*args,**kwargs)
			else:
				return redirect('/login/')
