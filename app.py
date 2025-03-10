from flask import Flask, render_template
from post import Post

app = Flask(__name__)

posts = [{"id":1, "titulo":"Contato", "categoria":"Blog", "img":"contact.jpg", "data":"09 February, 2025"}, {"id":2, "titulo":"App Finanças", "categoria":"App", "img":"webapp.jpg", "data":"28 February, 2025"}]
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["titulo"], post["categoria"], post["img"], post["data"])
    post_objects.append(post_obj)


@app.route("/")
def home():
    return render_template('site.htm', posts=post_objects)

@app.route('/blog/<int:post_id>')
def get_post(post_id):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == post_id:
            requested_post = blog_post

    return render_template('blog.htm', post=requested_post)


if __name__ == '__main__':
    app.run(debug=True)

