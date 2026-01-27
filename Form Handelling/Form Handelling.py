from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        name = request.form.get('email')
        password = request.form.get('password') 
        return "<b> Thanks For Logging in"
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)