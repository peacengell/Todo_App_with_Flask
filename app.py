import helper
from flask import Flask, request, Response
import json
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/item/new', methods=['POST'])
def add_item():
    # Get item from the POST body

    req_data = request.get_json()
    print(req_data)
    item = req_data['item']
    status = req_data['status']
    print(status)
    if status is None:
        res_data = helper.add_to_list(item, statu="Not Started")
    else:
        # Add item to the list
        res_data = helper.add_to_list(item, status)

    # Return error if item not added
    if res_data is None:
        response = Response("{'error': 'Item not added - '}" + item,
                            status=400,
                            mimetype='application/json')
        return response

    # return response
    response = Response(json.dumps(res_data), mimetype='application/json')

    return response


@app.route('/items/all')
def get_all_items():
    res_data = helper.get_all_items()

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response


@app.route('/item/status', methods=['GET'])
def get_item():
    # GET parameter from the url
    item_name = request.args.get('name')

    # Get items from the helper
    status = helper.get_item(item_name)

    #Return 4040 if item not found.
    if status is None:
        response = Response("{'error': 'Items Not found - %s'}" % item_name,
                            status=404,
                            mimetype='application/json')
        return response

    # Return status
    res_data = {'status': status}

    response = Response(json.dumps(res_data),
                        status=200,
                        mimetype='application/json')
    return response


@app.route('/item/update', methods=['PUT'])
def update_status():
    # Get item from the POST body
    req_data = request.get_json()
    item = req_data['item']
    status = req_data['status']

    # Update item in the list
    res_data = helper.update_status(item, status)

    #Return error if the status could not be updated

    if res_data is None:
        response = Response("{'error': 'Error updating item - '" + item +
                            ", " + status + "}",
                            status=400,
                            mimetype='application/json')
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response


@app.route('/item/remove', methods=['DELETE'])
def delete_item():
    # Get item from the Post body
    req_data = request.get_json()
    item = str(req_data['item'])

    # Delete item from the list
    res_data = helper.delete_item(item)

    # Delete error if the item could not be deleted
    if res_data is None:
        response = Response("{'error': 'Error deleting item - '" + item + "}",
                            status=400,
                            mimetype='application/json')

        return response
    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response


if __name__ == "__main__":

    app.run(debug=True)
