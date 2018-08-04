from flask import Flask,jsonify,request,Response
import json
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


def vaild_data(book_obj):
	if('name' in book_obj and 'price' in book_obj and 'isbn' in book_obj):

		return True
	else:
		return False


@app.route('/books',methods=['POST'])
#def add_book():
#	return jsonify(request.get_json())

def add_book():
	req_data=request.get_json()

	if(vaild_data(req_data)):
		new_book={"name":req_data["name"],

		"price":req_data["price"]
		,
		"isbn":req_data["isbn"]
		}
		books.insert(0,new_book)
		response_= Response("hdbsajbd",status =201,mimetype='application/json')
		response_.headers['Location']="/books/"+ 	str(new_book['isbn'])
		return response_
	else:
		inv_= {
		 "error":"Invalid object pased ",
		"help":"Data passed must be similar to {'name':bookname','price':5,'isbn':12132}"
		}
		response_=Response(json.dumps(inv_),status=400,mimetype="application/json")
		return response_

def valid_put_request(data):
	if("name" in data and "price" in data):
		return True
	else:
		return False

@app.route('/books/<int:isbn>',methods=["PUT"])
def replace_book(isbn):
	req_data=request.get_json()
	if (not valid_put_request(req_data)):
		inv_= {
		 "error":"Invalid object pased ",
		"help":"Data passed must be similar to {'name':bookname','price':5}"
		}
		response_=Response(json.dumps(inv_),status=400,mimetype="application/json")
		return response_
	new_book=	{
	"name":req_data["name"] ,

		"price":req_data["price"]
		,
		"isbn":isbn
		}

	i=0
	for book in books:
		if(book["isbn"]==isbn):
							books[i]=new_book

		i+=1
	response_=Response("",status=204)
	return response_


@app.route('/books/<int:isbn>',methods=['PATCH'])
def update_book(isbn):
	data=request.get_json()
	updated_book={}
	if("name" in data):
		updated_book["name"]=data["name"]
	if("price" in data):
		updated_book["price"]=data["price"]
	for i in books:
		if (i["isbn"]==isbn):
			i.update(updated_book)
	response_=Response("",status=204)
	response_.headers["Location"]="/books/"+str(isbn)
	return response_


@app.route('/books/<int:isbn>',methods=["DELETE"])
def delete_book(isbn):
	i=0
	for book in books:
		if book["isbn"]==isbn:
			books.pop(i)
			response_=Response("",status=204)
			return response_
		i+=1
	inv_={
	"error":"book iwth ISBN no that was provided was not found"
	}
	response_=Response(json.dumps(inv_),status=404,mimetype="application/json")
	return response_


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