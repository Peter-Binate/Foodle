from django.shortcuts import redirect, render
from django.core.mail import send_mail
from .models import Ingredient
from .forms import IngredientForm, ContactUsForm

# Create your views here.
def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    return render(request,
                  'ingredients/ingredient_list.html',
                  {'ingredients': ingredients})

def ingredient_detail(request, ingredient_id):
    ingredient = Ingredient.objects.get(id=ingredient_id)
    return render(request, 
                  'ingredients/ingredient_detail.html',
                  {'ingredient': ingredient})

def ingredient_create(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save()
            return redirect('ingredient-detail', ingredient.id)
    else:
        form = IngredientForm()
    
    return render(request,
                'ingredients/ingredient_create.html',
                {'form': form})

def ingredient_update(request, ingredient_id):
    ingredient = Ingredient.objects.get(id=ingredient_id)

    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('ingredient-detail', ingredient.id)
    else:
        form = IngredientForm(instance=ingredient)
    return render(request, 
                  'ingredients/ingredient_update.html',
                  {'form': form})

def ingredient_delete(request, ingredient_id):
    ingredient  = Ingredient.objects.get(id=ingredient_id)
    if request.method == 'POST':
        ingredient.delete()
        return redirect('ingredient-list')
    return render(request,
                'ingredients/ingredient_delete.html',
                {'ingredient': ingredient})

def contact(request):   
    if request.method == 'POST':
        # On créé une instance de notre formulaire et on le remplis avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via Foodle Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@foodle.xyz']
            )
        return redirect('email-sent')
    # si le formulaire n'est pas valide, On laisse l'exécution continuer jusqu'au return
    # ci-dessous et on affiche à nouveau le formulaire (avec des erreurs).
    else:
        form = ContactUsForm()

    return render(request,
                'ingredients/contact.html',
                {'form': form})