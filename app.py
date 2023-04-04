from flask import Flask,render_template, send_file

app=Flask('My Portfolio',template_folder='.')


@app.route('/')
def index():
    return render_template('main.html')

@app.route('/pic.jpg')
def get_bg():
    import requests
    r=requests.get('https://picsum.photos/1366/768',allow_redirects=True)
    with open('pic.jpeg','wb') as pic:
        pic.write(r.content)
    return send_file('pic.jpeg')

@app.route('/profile.jpg')
def get_dp():
    return send_file('profile.jpg')

if __name__ == '__main__':
    app.run(debug=True)