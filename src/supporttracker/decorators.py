from django.shortcuts import render, redirect

def profile_required():
	create_profile_url = settings.CREATE_PROFILE_URL

	def _dec(view_func):
		def _view(request,*args,**kwargs):
			try:
				user.userprofile
				return view_func(request,*args,**kwargs)
			except UserProfile.DoesNotExist:
				return redirect('/create_user_profile/')
