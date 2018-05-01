from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string


def create_user(username=None, password=None, **kwargs):
    User = get_user_model()
    if username is None:
        username = kwargs.get(User.USERNAME_FIELD)

    if not username:
        username = get_random_string()

    kwargs.update({
        User.USERNAME_FIELD: username,
    })

    user = User.objects.create(**kwargs)
    if password:
        user.set_password(password)
        user.save()
    return user
