from flask import Flask,render_template

app=Flask('My Portfolio',template_folder='.')


@app.route('/')
def index():
    return render_template('main.html')

@app.route('/bg')
def get_bg():
    import requests
    r=requests.get('https://picsum.photos/200/300',allow_redirects=True)
    return r.content

if __name__ == '__main__':
    app.run(debug=True)