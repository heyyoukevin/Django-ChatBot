from django.shortcuts import render, redirect
from .models import Conversation

def chatbot(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        Conversation.objects.create(question=question, answer='Thank you', ip_address=request.META.get('REMOTE_ADDR'))
        return redirect('chatbot')
    conversations = Conversation.objects.all().order_by('-date', '-time')
    return render(request, 'chatapp/chatbot.html', {'conversations': conversations})

def history(request):
    conversations = Conversation.objects.all().order_by('-date', '-time')
    return render(request, 'chatapp/history.html', {'conversations': conversations})