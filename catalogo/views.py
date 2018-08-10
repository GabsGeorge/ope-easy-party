from django.shortcuts import render, get_object_or_404
from catalogo.models import Categoria
from catalogo.models import Produto
from django.views import generic
# Create your views here.

#Categorias
class CategoriaListView(generic.ListView):
    template_name = 'catalogo/categoria.html'
    context_object_name = 'produtos'
    
    def get_queryset(self):
        return Produto.objects.filter(categoria_p__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoriaListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Categoria, slug=self.kwargs['slug'])
        return context    
    paginate_by = 8

categoria = CategoriaListView.as_view() 

#Listatgem de produtos
class ListProdutoView(generic.ListView):
    model = Produto
    template_name = 'catalogo/lista_produto.html'
    context_object_name = 'produtos'
lista_produto = ListProdutoView.as_view()

#Produto unico
def produto(request, slug):
    produto = Produto.objects.get(slug=slug)
    contexto = {
        'produto_atual': produto,
        'categorias':Categoria.objects.all()
    }
    return render(request, 'catalogo/produto.html', contexto)      