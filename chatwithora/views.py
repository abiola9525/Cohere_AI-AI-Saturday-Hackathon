from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . cohere_api import get_chatbot_response, summerizer
from django.contrib.auth.decorators import login_required




@login_required
def chat(request):
    return render(request, 'chat.html')

@csrf_exempt
def ask(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        bot_response = get_chatbot_response(user_input)
        return JsonResponse(bot_response, safe=False)
    else:
        return JsonResponse({'error': 'Invalid'}, safe=False)
    
@login_required
def sum_page(request):
    return render(request, 'summerize.html')

@csrf_exempt
def summerize(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        bot_response = summerizer(user_input)
        return JsonResponse(bot_response, safe=False)
    else:
        return JsonResponse({'error': 'Invalid'}, safe=False)

