from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models.customer import Customer

@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def save_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = UserProfile(user=user)
        profile.save()
        
@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance, name=instance.username, email=instance.email)

@receiver(post_save, sender=User)
def save_customer(sender, instance, **kwargs):
    instance.customer.save()


