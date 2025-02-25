from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('site.htm')

@app.route("/blog_post")
def blog_post():
    return render_template('blog.htm')


if __name__ == '__main__':
    app.run(debug=True)

