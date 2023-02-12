from django.shortcuts import render, get_object_or_404

from .models import BonusCard


def home(request):
    cards = BonusCard.objects.all()
    context = {
        'cards': cards,
    }
    return render(request, 'bonus_card/home.html', context)


def detail(request, pk):
    card = get_object_or_404(BonusCard, pk=pk)
    context = {
        'card': card,
    }
    return render(request, 'bonus_card/detail.html', context)
