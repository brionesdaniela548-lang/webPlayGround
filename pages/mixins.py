from django.contrib.auth.mixins import LoginRequiredMixin

class LoginRequiredMixinCustom(LoginRequiredMixin):
    login_url = '/accounts/login/'