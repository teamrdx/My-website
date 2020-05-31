from flask import Flask, render_template, request

app = Flask(__name__, template_folder = 'template')
import csv
@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/contact.html')
def contact_page():
    return render_template('contact.html')


def write_to_file(data):
	with open('database.txt', mode = 'a') as database:
		name = data["name"]
		email = data["email"]
		message = data["message"]
		file = database.write(f'\n {name}, {email}, {message}')


def write_to_csv(data):
	with open('database.csv', newline = '', mode = 'a') as database2:
		name = data["name"]
		email = data["email"]
		message = data["message"]
		csv_writer = csv.writer(database2, delimiter = ',' , quotechar = '"', quoting = csv.QUOTE_MINIMAL )
		csv_writer.writerow([name, email, message])





@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_csv(data)
		return render_template('thankyou.html')
	else:
		return "Something went Wrong"