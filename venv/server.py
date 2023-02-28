from flask import Flask, render_template
import random
import datetime
import requests


app = Flask(__name__, template_folder='templates')
age_api = "https://api.agify.io?name="
gender_api = "https://api.genderize.io?name="
blog_url = "https://api.npoint.io/a638783ab8608716d37f"


def get_year():
    current_year = datetime.datetime.now().year
    return current_year


@app.route('/')
def home():
    #return "hello world"
    #current_year = datetime.datetime.now().year
    random_number = random.randint(1, 10)
    return render_template("new-blog/index.html", rand_num=random_number, cur_year=get_year())


@app.route('/guess/<name>')
def guess(name):
    age_api_response = requests.get(f"{age_api}{name}")
    age_api_response_dict = age_api_response.json()
    print(type(age_api_response_dict))
    print(f"{age_api_response_dict['age']}")
    gender_api_response = requests.get(f"{gender_api}{name}")
    gender_api_response_dict = gender_api_response.json()
    return render_template("guess-template/index.html",
                           age_api_data=age_api_response_dict,
                           cur_year=get_year(),
                           gender_api_data=gender_api_response_dict)


@app.route('/blog')
def blog():
    blog_url_response = requests.get(blog_url)
    blog_url_response_json = blog_url_response.json()
    return render_template("blog-template/index.html", blog_data=blog_url_response_json)


@app.route('/blog/<test_num>')
def get_blog(test_num):
    blog_url_response = requests.get(blog_url)
    blog_url_response_json = blog_url_response.json()
    return render_template("blog-template/index.html", blog_data=blog_url_response_json, test_num=test_num)
    # above test_num is a new parameter coming from the index.html being passed back into the function back into the
    # webpage to use. SO the parameter comes from example-template/index.html passed into this function then passed
    # to the blog-template/index.html to be used.


if __name__ == "__main__":
    app.run(debug=True)
