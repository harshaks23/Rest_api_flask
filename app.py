from flask import Flask,jsonify,request,Response

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



@app.route('/books',methods=['POST'])
#def add_book():
#	return jsonify(request.get_json())

def add_book():
	req_data=request.get_json()

	if(vaild_data(req_data)):
		new_book={"name":req_data["name"],

		"price":req_data["price"]
		,
		"isbn":req_data[isbn]
		}
		books.insert(0,new_book)
		response_= Response("",201,mimetype())




#by default get method
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





# search http://127.0.0.1:5000/books/123456		

app.run(port=5000,debug=True)