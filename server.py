from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template("./index.html")


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'

    else:
        return 'something went wrong. Try again!'


# app = Flask(__name__): to instantiate a member of the Flask class called app.
# @app.route('/') is a generator used to create a directory on our website.
# @app.route('/blog) is a generator used to create a sub-directory on our website.
# Just save it as hello.py or something similar. Make sure to not call your application flask.py because this would conflict with Flask itself.
# instead of just saving text documents into our server, flask has another function called render_template that can be used to serve html files.
# but we need to create a folder called templates and save all the html files into this folder
# render_template allows us to serve multiple html files at once.
# in order to be able to serve our css and js files(flask static files),
# we need to create a folder called static and save these files into this
# folder.
