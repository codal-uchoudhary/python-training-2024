from django import dispatch
from django.dispatch import receiver
from django.contrib.auth.models import User
from blog.models import Post
from django.db.models.signals import pre_delete, post_save, post_delete
from django.contrib.auth.signals import user_logged_in, user_logged_out


@receiver(post_save, sender=Post)
def post_save_receiver(sender, instance, **kwargs):
    print(f"{instance.title} is saved")


@receiver(pre_delete, sender=Post)
def action_user_login(sender, instance, **kwargs):
    print(f"{instance.title} :blog is deleted ")
