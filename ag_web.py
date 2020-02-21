from flask import Flask, render_template, url_for
app = Flask(__name__)

datos = [
	{
	'autor':'Marcelo',
	'texto':'LADEROOOOOOOOOOOOOOOOOOOOOOOOOOOOO'
	},
	{
	'autor':'Paloma',
	'texto':'Paloma227'
	},
	{
	'autor':'Japo',
	'texto':'Japon Japon PON PON PON'
	}

]

@app.route('/')
def hello():
    return render_template('home.html', info=datos)

@app.route('/about')
def about():
    return render_template('about.html', title='About')


# debug
if __name__ == '__main__':
	app.run(debug=True)