# myapp/decorators.py
from django.http import HttpResponseForbidden
from functools import wraps

def roles_required(allowed_roles=[]):
    def decorator(view_func):
        @wraps(view_func)
        def wrap(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("You don't have permission to access this page.")
        return wrap
    return decorator


from django.contrib.auth.decorators import permission_required

@permission_required('app_name.permission_codename')
def my_view(request):
    # Your view logic here
    return render(request, 'template.html')

# news/models.py
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        permissions = [
            ("can_publish", "Can publish articles"),
        ]


"""
{% if perms.app_name.permission_codename %}
    <!-- Content to display if the user has the permission -->
    <p>You have permission to do this!</p>
    <a href="{% url 'some_view' %}">Do something</a>
{% else %}
    <!-- Content to display if the user does not have the permission -->
    <p>You do not have permission to do this.</p>
{% endif %}

"""