from django.conf import settings

def add_variable_to_context(request):
    user = request.user
    # print(user.employee)
    return {
        'server_image': settings.SERVER_IMAGE,
        'user': user
    }