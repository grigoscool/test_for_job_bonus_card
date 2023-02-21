import random
from datetime import timedelta

from django.views import generic
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import BonusCard, Buy
from .forms import BonusCardForm


def home(request):
    """ Show list of all bonus cards. """
    bonus_card = BonusCard.objects.all()

    paginator = Paginator(bonus_card, 3)
    paginator_page = request.GET.get('page')
    cards = paginator.get_page(paginator_page)

    context = {
        'cards': cards,
    }
    return render(request, 'bonus_card/home.html', context)


def detail(request, pk):
    """ Show detail info about card. """
    card = get_object_or_404(BonusCard, pk=pk)
    buys = Buy.objects.filter(bonus_card_id=pk)
    if card.date_end <= timezone.now():
        card.overdue = True
    context = {
        'card': card,
        'buys': buys,
    }
    return render(request, 'bonus_card/detail.html', context)


def search(request):
    """ Show results of searching. """
    query = request.GET.get('search')
    card = BonusCard.objects.search(query)
    context = {
        'card': card,
    }
    return render(request, 'bonus_card/search.html', context)


def activate(request, pk):
    """ Change activate into True. """
    activate_card = get_object_or_404(BonusCard, pk=pk)
    activate_card.activate = True
    activate_card.save()
    return redirect('bonus_card:detail', pk=pk)


def deactivate(request, pk):
    """ Change activate into False. """
    deactivate_card = get_object_or_404(BonusCard, pk=pk)
    deactivate_card.activate = False
    deactivate_card.save()
    return redirect('bonus_card:detail', pk=pk)


def delete(request, pk):
    """ Delete bonus card. """
    delete_card = get_object_or_404(BonusCard, pk=pk)
    delete_card.delete()
    return redirect('bonus_card:home')


def generate_card(request):
    """ Show page with form to generate custom bonus card. """
    return render(request, 'bonus_card/generate_card.html')


def generate(request):
    """ This view will create custom bonus card. """
    my_list = list(range(1_000, 10_000))
    for _ in range(int(request.GET.get('count_cards'))):
        BonusCard.objects.create(
            serial_num=int(request.GET.get('serial')),
            card_num=random.sample(my_list, k=1)[0],
            date_creation=timezone.now(),
            date_end=(timezone.now() +
                      timedelta(days=int((request.GET.get('duration'))) * 30)),
        )
    return redirect('bonus_card:home')


class CreateCard(generic.CreateView):
    """
    This view show a form to create bonus card.
    """
    form_class = BonusCardForm
    template_name = 'bonus_card/add_card.html'
