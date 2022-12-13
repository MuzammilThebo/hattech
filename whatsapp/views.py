from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse


conversations = {
        "Hi": "Welcome to EngageX WorkShop 1.0",
        "Hello": "Welcome to EngageX WorkShop 1.0",
        "How Are You": "I am Fine, What About You?",
        "Wifi": """
        SSID: AIO-021
        Pass : AI@_0210"""
    }

@csrf_exempt
def message(request):
    user = request.POST.get('From')
    message = request.POST.get('Body')
    print(f'{user} says {message}')

    response = MessagingResponse()
    response.message(conversations.setdefault(message, "Sorry, Can you Ask me another Question"))
    return HttpResponse(str(response))
