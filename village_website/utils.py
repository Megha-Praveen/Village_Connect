from django.contrib.auth import get_user_model
from .models import UserInfo

def authenticate_house_no(request, house_no=None, password=None):
    User = get_user_model()
    try:
        user_info = UserInfo.objects.get(house_no=house_no)
        user = User.objects.get(pk=user_info.user_id)
        if user.check_password(password):
            return user
    except UserInfo.DoesNotExist:
        pass
    return None