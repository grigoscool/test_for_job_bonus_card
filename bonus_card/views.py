from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import BonusCard


def home(request):
    """ Show list of all bonus cards """
    cards = BonusCard.objects.all()
    context = {
        'cards': cards,
    }
    return render(request, 'bonus_card/home.html', context)


def detail(request, pk):
    """ Show detail info about card """
    card = get_object_or_404(BonusCard, pk=pk)
    context = {
        'card': card,
    }
    return render(request, 'bonus_card/detail.html', context)


def search(request):
    """ Show results of searching """
    search_item = request.GET.get('search')
    card = BonusCard.objects.filter(
        Q(card_num__icontains=search_item) | Q(serial_num__icontains=search_item) |
        Q(date_creation__icontains=search_item) | Q(date_end__icontains=search_item))
    context = {
        'card': card,
    }
    return render(request, 'bonus_card/search.html', context)