from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/greet', methods =['GET'])

def greet():
   fname = request.args.get("fname")
   lname = request.args.get('lname')
   if not fname and not lname:
    return jsonify({"status": "error"})
   elif fname and not lname:
    response = {
      'data': f'fnmae'}
   elif not fname and lname:

    response = {
        "data": f'Hello, {lname}!'
    }
   else:
    return jsonify(response)


if __name__ == '__main__':
    app.run()