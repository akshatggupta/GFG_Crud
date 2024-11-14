from flask import Flask, request, jsonify

app = Flask(__name__)

#Sample data 
items =[
    {"id": 1, "name": "John", "address": "New York"},
    {"id": 2, "name": "Doe", "address": "California"},
    {"id": 3, "name": "Smith", "address": "Texas"},
    {"id": 4, "name": "David", "address": "Florida"}
]

#Crud Apllication

#Get all items
@app.route('/items', methods=['GET'])
def get_all_items():
    return jsonify(items)

#Get single item
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    for item in items:
        if item["id"] == item_id:
            return jsonify(item)   #return item if found in json format
    return jsonify({"message": "Item not found"}), 404  #throw error if item not found
    

#Add new item
@app.route('/items', methods=['POST'])
def add_item():
    new_item = {'id': request.json['id'], 'name': request.json['name'], 'address': request.json['address']}  #accept all parameter in json format
    items.append(new_item)
    return jsonify(new_item)

#Update item
@app.route('/items/<int:item_id>', methods=['PUT'])
def upadte_info(item_id):
    for item in items:
        if item['id']==item_id:
            item['name'] = request.json['name']
            item['address'] = request.json['address']
            return jsonify(item) 
    return jsonify({"message": "Item not found"}), 404  #throw error if item not found

#Delete item
@app.route('/items<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    for item in items:
        if item['id']==item_id:
            items.remove(item)
            return jsonify({"message": "Item deleted"})
    return jsonify({"message": "Item not found"}), 404  

if __name__ == '__main__':
    app.run(debug=True)

