import csv
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def myHome():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_csv(data)
            return '', 204
        except:
            return 'Did not save a message to contact', 400
    else:
        return 'Something went wrong', 400
    
def write_csv(data):
    with open('contact.csv', mode='a', newline='') as db:
        name = data['Name']
        email = data['Email']
        subject = data['Subject']
        message = data['Message']
        csv_writer = csv.writer(db, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message])
