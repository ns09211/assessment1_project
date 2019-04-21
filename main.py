from flask import Flask, request, jsonify
import models

app = Flask(__name__)

@app.route('/create/user', methods=["POST"])
def new_user():
    if request.form.get("add_data") == 'Submit':
        u_name = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        p_number = request.form.get('ph_num')
    user_data = {'Username':u_name, 'Password':password, 'Email':email,'Phone':p_number}
    if models.form_request(user_data) == "User added Successfully":
        return jsonify({"Response-code":"200","Response-message":"User Added Successfully"})
    elif models.form_request(user_data) == "User updated Successfully":
        return jsonify({"Response-code":"200","Response-message":"User Updated Successfully"})
    else:
        return jsonify({"Response-code":"417","Response-message":"Task Failed due to Exception"})

@app.route('/find/user', methods=["POST"])
def find_user():
    if request.form.get("find_data") == 'Search':
        email = request.form.get('u_email')
        data = {"Email":email}
    response = models.form_request(data, search=True)
    if models.form_request(data, search=True) == "User Not Found":
        return jsonify({"Response-code":"404","Response-message":"User Added Successfully"})
    else:
        return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
