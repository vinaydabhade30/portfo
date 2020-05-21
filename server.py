from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def title_page():
    return render_template('index.html')

@app.route('/<string:page_name>')
def index(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', 'a') as fl:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = fl.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as file:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_file = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return "something went wrong. Try again"

