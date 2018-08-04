from flask import Flask,jsonify

app= Flask(__name__)
print(__name__)

books=[
{
	'name':'ksh',
	'price':23,
	'isbn':123456

},
{
	'name':'esh',
	'price':18,
	'isbn':123457
	}

]

@app.route('/')
@app.route('/books')
def hello_world():
	return jsonify(books)


@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
	ret={}
	for i in books:
		if i["isbn"]==isbn:
			ret={
			'name':i['name'],
			'price':i['price']
			}
	return jsonify(ret)


app.run(port=5000,debug=True)