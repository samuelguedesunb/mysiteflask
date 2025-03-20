from flask import Flask, render_template, request, redirect, url_for, flash
from post import Post

app = Flask(__name__)
app.secret_key = '624007eff499cf1e493cb8043e94f740'  # Necessário para usar flash messages

posts = [{"id":1, "titulo":"Contato", "categoria":"Blog", "img":"contact.jpg", "data":"09 February, 2025", "body":"<p>Gostou do conteúdo e quer conversar? Ficarei feliz em ouvir você! Você pode entrar em contato comigo através das minhas redes sociais ou enviar um e-mail diretamente para samuelguedesunb@gmail.com.</p>"},
         {"id":2, "titulo":"App Finanças", "categoria":"App", "img":"webapp.jpg", "data":"28 February, 2025", "body":"<p>Um aplicativo que permite gerar gráficos a partir de planilhas Google</p>"}]
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["titulo"], post["categoria"], post["img"], post["data"], post["body"])
    post_objects.append(post_obj)


@app.route("/")
def home():
    return render_template('site.htm', posts=post_objects, active_page='home')

@app.route('/blog/<int:post_id>')
def get_post(post_id):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == post_id:
            requested_post = blog_post
            break

    if requested_post is None:
        return "Post não encontrado", 404

    # Definir se o formulário deve ser exibido (apenas para o post com id 3, por exemplo)
    exibir_formulario = requested_post.id == 1

    return render_template('blog.htm', post=requested_post, exibir_formulario=exibir_formulario)

    #return render_template('blog.htm', post=requested_post)

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        # Processar os dados do formulário
        nome = request.form['nome']
        email = request.form['email']
        mensagem = request.form['mensagem']

        # Aqui você pode adicionar a lógica para enviar um email, salvar no banco de dados, etc.
        print(f"Nome: {nome}, Email: {email}, Mensagem: {mensagem}")

        # Exibir uma mensagem de sucesso
        flash('Mensagem enviada com sucesso!', 'success')
        return redirect(url_for('contato'))

    # Se for um GET, apenas renderize o formulário
    requested_post = post_objects[0]
    return render_template('blog.htm', post=requested_post, exibir_formulario=True)


if __name__ == '__main__':
    app.run(debug=True)

