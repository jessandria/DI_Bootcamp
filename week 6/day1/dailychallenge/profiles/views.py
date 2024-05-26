from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Profile

@csrf_exempt
def create_profile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        profile = Profile.objects.create(name=name, email=email)
        return JsonResponse({'success': True, 'profile_id': profile.id})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

@csrf_exempt
def delete_profile(request, id):
    try:
        profile = Profile.objects.get(id=id)
        profile.delete()
        return JsonResponse({'success': True})
    except Profile.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Profile not found'})