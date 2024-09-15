from flask import Flask, render_template

app = Flask(__name__)

posts={
    0:{
        'title':'Hello World!',
        'content':'This is my first blog post!'
    }
}

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/post/<int:post_id>')
def post(post_id):
    post= posts.get(post_id)
    return render_template('posts.html')

if __name__ == '__main__':
    app.run(debug=True)


