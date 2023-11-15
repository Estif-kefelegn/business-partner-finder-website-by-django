from django.db.models.signals import post_save, post_delete # THIS METHOD TRIGGERED WHEN THE SAVE METHOD IS CALLED
from django.dispatch import receiver # weare going to use @reciver decorator


from django.contrib.auth.models import User
from .models import Profile

# @receiver(post_save, sender=Profile)    
def createProfile(sender, instance, created, **kwargs): #while we create a user we create a profile dinamically 
    if created:
        user = instance # instance means the profile ==== sender=User
        profile = Profile.objects.create(
            user = user,
            username= user.username,
            email = user.email,
            name= user.first_name
            
        )
    

def profileDelete(sender, instance, **kwargs):
    user = instance.user
    user.delete()
   
    
post_save.connect(createProfile, sender=User) # we create and save it here        
post_delete.connect(profileDelete, sender=Profile)