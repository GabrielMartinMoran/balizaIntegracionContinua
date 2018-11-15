from flask import Flask, request, jsonify, render_template


USERNAME = "MrKupo"
REPOSITORY = "test_ci"
VALID_TOKEN = "_6ExBju88GSiQvq-m4Rc"
SERVER_DOMAIN = "http://localhost"
PORT=8080

build_status = "success"

app = Flask(__name__)

def has_valid_headers(headers):
    token = None
    print(headers)
    try:
        token = headers['PRIVATE-TOKEN']
    except:
        return False
    if (VALID_TOKEN == token):
        return True
    return False

def generate_build_state():
    return [
        {
            "status": build_status
        }
    ]

@app.route('/projects/<username>/<repository>/pipelines', methods=['GET'])
def get_build_satus(username, repository):
    headers_valid = has_valid_headers(request.headers)
    print("HEADERS VALID:",headers_valid)
    if(not headers_valid or username != USERNAME or repository != REPOSITORY):
        return jsonify({'message': '401 Unauthorized'})
    build_state = generate_build_state()
    print(username, repository, build_state)
    return jsonify(build_state)

@app.route('/config', methods=['GET'])
def config():
    return render_template("config.html", SERVER_URL=SERVER_DOMAIN+":"+str(PORT))

@app.route('/set_status/<status>', methods=['GET'])
def set_build_satus(status):
    global build_status
    build_status = status
    return "OK"

def run_app():
    app.run(host="0.0.0.0",port=PORT)

if __name__ == '__main__':
    run_app()