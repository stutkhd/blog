from django.views.generic import DetailView, ListView
from blog.models import Post

# ListView -> モデルのデータ一覧を表示する画面に使われる
# 自動で該当のモデルを取得し、TemplateResponseを作成して値を返す
class PostListView(ListView):
    model = Post # 一覧で表示させたいモデル
    ordering = '-created_at' # -が先頭につくと降順になる
    template_name = "post_list.html" # 表示に使われるテンプレート
    context_object_name = 'posts' # 取得したモデルの一覧を、テンプレート内で使うときの名前

# DetailView -> ListViewで指定した属性に加えて
# どの変数名でURLからIDを取得するかをpk_url_kwargsで指定する
class PostDetailView(DetailView):
    model = Post
    pk_url_kwarg = "post_id" # pk=primary key
    template_name = 'post_detail.html'
    context_object_name = 'post'