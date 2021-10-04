from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages

from core import models, forms


def index(request):
    contatos = models.Contato.objects.filter(ativo=True).order_by('nome')

    context = {
        'contatos': contatos
    }

    return render(request, 'core/index.html', context)


def cadastrar_e_editar_contato(request, pk=None):
    contato = None

    if pk:
        contato = get_object_or_404(
            models.Contato,
            pk=pk,
            ativo=True
        )

    form = forms.ContatoForm(instance=contato)

    if request.method == 'POST':
        form = forms.ContatoForm(
            data=request.POST,
            instance=contato
        )

        if form.is_valid():
            form.save()
            
            if contato:
                messages.success(request, 'Contato alterado com sucesso!')
            else:
                messages.success(request, 'Contato cadastrar com sucesso!')

        else:
            if contato:
                messages.warning(request, 'Falha ao editar contato!')
            else:
                messages.warning(request, 'Falha ao cadastrar contato!')

        return redirect('index')

    context = {
        'form': form,
        'instance': contato
    }

    return render(request, 'core/cadastro.html', context)


def excluir_contato(request, pk):
    contato = get_object_or_404(
        models.Contato,
        pk=pk,
        ativo=True
    )
    contato.excluir()
    messages.success(request, 'Contato excluído com sucesso!')
    return redirect('index')
