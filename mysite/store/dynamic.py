from .models import User, Image
from .forms import UserForm
from .services import get_images


def contact_email(request):
    email = User()
    form = UserForm(request.POST, instance=email)
    if request.POST:
        if form.is_valid():
            email.save()
    ctx = {
        'form_email': form
    }
    return ctx


def footer_image(request):
    images = get_images()
    ctx = {
        "images": images
    }
    return ctx
