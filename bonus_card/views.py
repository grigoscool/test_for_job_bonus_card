import random
import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from .models import BonusCard, Buy


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
    buys = Buy.objects.filter(bonus_card_id=pk)
    print(card.date_end)
    context = {
        'card': card,
        'buys': buys,
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


def activate(request, pk):
    activate_card = get_object_or_404(BonusCard, pk=pk)
    activate_card.activate = True
    activate_card.save()
    return redirect('bonus_card:detail', pk=pk)


def deactivate(request, pk):
    deactivate_card = get_object_or_404(BonusCard, pk=pk)
    deactivate_card.activate = False
    deactivate_card.save()
    return redirect('bonus_card:detail', pk=pk)


def delete(request, pk):
    delete_card = get_object_or_404(BonusCard, pk=pk)
    delete_card.delete()
    return redirect('bonus_card:home')


def generate_card(request):
    return render(request, 'bonus_card/generate_card.html')


def generate(request):
    my_list = [i for i in range(1_111, 10_000)]
    for _ in range(int(request.GET.get('count_cards'))):
        new_card = BonusCard.objects.create(
            serial_num=int(request.GET.get('serial')), card_num=random.sample(my_list, k=1)[0],
            date_creation=datetime.datetime.now(), date_end='2023-12-27 08:29:07+00:00',
        )
    return redirect('bonus_card:home')