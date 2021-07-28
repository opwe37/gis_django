from django.http import HttpResponseForbidden

from profileapp.models import Profile


def profile_ownership_required(func):
    def decorated(requset, *args, **kwargs):
        target_profile = Profile.objects.get(pk=kwargs['pk'])
        if target_profile.user == requset.user:
            return func(requset, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return decorated

