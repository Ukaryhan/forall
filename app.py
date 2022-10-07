
from flask import request, Flask, jsonify

from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from

app = Flask(__name__)

###########------------------------------------------------------------------##################

app.json_encoder = LazyJSONEncoder

swagger_template = dict(
    info = {
        'title': LazyString(lambda:'API Documentation for Data Processing and Modeling'),
        'version': LazyString(lambda:'1.0.0'),
        'description': LazyString(lambda:'Dokumentasi API untuk Data Processing dan Modeling')
        }, host = LazyString(lambda: request.host)
    )

swagger_config = {
        "headers":[],
        "specs":[
            {
            "endpoint":'quiz_3',
            "route":'/quiz_3.json'
            }
        ],
        "static_url_path":"/flasgger_static",
        "swagger_ui":True,
        "specs_route":"/quiz_3/"
    }

swagger = Swagger(app, template=swagger_template, config=swagger_config)

###########------------------------------------------------------------------##################

languages=[{'name':'Javascript'},{'name':'Python'},{'name':'Ruby'}]

###########------------------------------------------------------------------##################

#Get
@swag_from("quiz_3/index.yml", methods=["GET"])
@app.route('/', methods=['GET'])
def test():
	return jsonify({'Message' : 'It Works' })

@swag_from("quiz_3/index.yml", methods=["GET"])
@app.route('/lang', methods=['GET'])
def returnAll():
	return jsonify({'languages' : languages })

###########------------------------------------------------------------------##################

#Get2
@swag_from("quiz_3/lang_get.yml", methods=["GET"])
@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
	langs = [language for language in languages if language['name'] == name]
	return jsonify({'language' : langs[0]})

###########------------------------------------------------------------------##################

#Post
@swag_from("quiz_3/lang_post.yml", methods=["POST"])
@app.route('/lang', methods=['POST'])
def addOne():
	language = {'name':request.json['name']}

	languages.append(language)
	return jsonify ({'language':languages})

###########------------------------------------------------------------------##################

#PUT
@swag_from("quiz_3/lang_put.yml", methods=["PUT"])
@app.route('/lang/<string:name>', methods=['PUT'])
def editOne(name):
	langs=[language for language in languages if language['name']==name]
	langs[0]['name']=request.json['name']
	return jsonify ({'language':langs[0]})

###########------------------------------------------------------------------##################

#DELETE
@swag_from("quiz_3/lang_delete.yml", methods=["Delete"])
@app.route('/lang/<string:name>', methods=['DELETE'])
def removeOne(name):
	lang=[language for language in languages if language['name']==name]
	languages.remove(lang[0])
	return jsonify({'language':languages})

###########------------------------------------------------------------------##################

if __name__=='__main__':
	app.run()


