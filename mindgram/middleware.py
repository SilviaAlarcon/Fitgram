#Fitgram middleware catalog. https://docs.djangoproject.com/en/2.0/topics/http/middleware/

#Django
from django.shortcuts import redirect
from django.urls import reverse

'''
Profile completion middleware
Ensure every user that is interacting with the platform 
have their profile picture and biography.
'''
class ProfileCompletionMiddleware:
    # Middleware initialization.
    def __init__(self, get_response):
        self.get_response = get_response
       
    #Code to be execute for each request before the view is called
    def __call__(self, request):
        #Verify that there is an active session 
        if not request.user.is_anonymous:
            #allows staff not to have biography and picture 
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    #this is the same as if request.path != users/me/profile and users/logout
                    if request.path not in [reverse('users:update'), reverse('users:logout')]: 
                        return redirect('users:update')

        responde = self.get_response(request)

        return responde

