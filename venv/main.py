from flask import Flask, render_template
import requests


app = Flask(__name__)
blog_url = "https://api.npoint.io/a638783ab8608716d37f"


@app.route('/')
def home():
    blog_url_response = requests.get(blog_url)
    blog_url_response_json = blog_url_response.json()
    return render_template("blog/index.html", blog_data=blog_url_response_json)


@app.route('/blog/<id>')
def get_blog(id):
    blog_url_response = requests.get(blog_url)
    blog_url_response_json = blog_url_response.json()
    for post in blog_url_response_json:
        if int(id) == int(post['id']):
            post_data = {
                "id": id,
                "title": post['title'],
                "subtitle": post['subtitle'],
                "body": post['body']
            }
    return render_template("blog/post.html", post_data=post_data, blog_id=id)


if __name__ == "__main__":
    app.run(debug=True)
