from flask import Flask, jsonify


app = Flask(__name__)

vases =[{'name': 'omg number 1',
            'price':100,
            'volume':2},
        {'name': 'omg number 2',
            'price':110,
            'volume':3},
        {'name': 'omg number 3',
            'price':120,
            'volume':1}
        ]


@app.route('/')
def index():
    return "Nothing is the start for the universe"

@app.route("/vases", methods=['GET'])
def get():
    return jsonify(vases)

@app.route("/vases/<int:id>", methods=['GET'])
def get_by_id(id):
    return jsonify({'Vase with id=%d'%id: vases[id]})

@app.route("/vases/", methods=['POST'])
def create():
    vase = {'name': 'omg number 4',
            'id': 3,
            'price':'140',
            'volume':'0.2'}
    vases.append(vase)
    return jsonify({'Created':vase})

@app.route("/vases/<int:id>", methods=['PUT'])
def update(id):
    vases[id]['name'] = "updated name"
    vases[id]['price'] = "updated price"
    vases[id]['volume'] = "updated volume"
    return jsonify({"Updated with id=%d"%id: vases[id]})

@app.route("/vases/<int:id>", methods=['DELETE'])
def delete(id):
    vases.remove(vases[id])
    return jsonify({"Deleted with id=%d"%id: True})

if __name__ == '__main__':
    app.run(debug=True)