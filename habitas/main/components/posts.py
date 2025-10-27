from django_unicorn.components import UnicornView
from ..models import Tree, Post


class PostsView(UnicornView):
    tree: Tree = None
    posts: Post = None
    content: str = ""
    error: str = ""

    def mount(self):
        self.posts = Post.objects.filter(tree=self.tree)
        return super().mount()

    def update(self, id):
        self.tree = Tree.objects.get(id=int(id))
        self.posts = Post.objects.filter(tree=self.tree)

    def submit(self):
        if not self.content:
            self.error = "Por favor, escreva um comentário"
            return
        
        if not self.request.user.is_authenticated:
            self.error = "Você precisa estar logado para comentar"
            return
        
        # Verifica se o usuário é técnico ou gestor automaticamente
        is_specialized = False
        if hasattr(self.request.user, 'is_tecnico') and hasattr(self.request.user, 'is_gestor'):
            is_specialized = self.request.user.is_tecnico() or self.request.user.is_gestor()
        
        Post.objects.create(
            tree=self.tree,
            author=self.request.user.username,
            content=self.content,
            specialized=is_specialized
        )
        
        # Reset
        self.content = ""
        self.error = ""
        self.posts = Post.objects.filter(tree=self.tree)

