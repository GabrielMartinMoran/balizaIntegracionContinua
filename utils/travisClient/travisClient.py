import requests
from BuildStatus import BuildStatus

#https://docs.travis-ci.com/api/#builds

#TRAVIS_API_URL = "https://api.travis-ci.org"
TRAVIS_API_URL = "http://127.0.0.1:8080"

def get_status(github_username, repository_name, travis_token):
    #Definimos los headers para el request
    headers = {
        "Travis-API-Version": "3",
        "Authorization": "token " + travis_token
    }
    response = None
    try:
        response = requests.get(TRAVIS_API_URL + "/repo/"+ github_username +"%2F"+ repository_name + "/builds?limit=1&sort_by=finished_at:desc", headers=headers)
    except requests.exceptions.ConnectionError:
        #Si existe error de conexion
        return BuildStatus.CONNECTION_ERROR
    #Si existe algun problema de credenciales, usuario o repositorio incorrectos
    if(response.text == "access denied"):
        return BuildStatus.ACCESS_DENIED
    json_response = response.json()
    #Si no fue compilado nunca
    if(len(json_response['builds']) == 0):
        return BuildStatus.NOT_YET_BUILT
    build_status = json_response['builds'][0]['state']
    #Si paso los tests
    if(build_status == "passed"):
        return BuildStatus.PASSED
    #Si fallo los tests
    elif(build_status == "failed"):
        return BuildStatus.FAILED
    else:
        #Si en este momento esta corriendo los tests
        return BuildStatus.RUNNING

ci_public_access_token = "9cHb1xMQyaGSSSsi6xTW5Q"
repository_name = "dyasc-2018"
git_login_username = "MrKupo"
status = get_status(git_login_username, repository_name, ci_public_access_token)
print(status)

def test_status(github_username, repository_name, travis_token):
    #Definimos los headers para el request
    headers = {
        "Travis-API-Version": "3",
        "Authorization": "token " + travis_token
    }
    response = None
    response = requests.get(TRAVIS_API_URL + "/repo/"+ github_username +"%2F"+ repository_name + "/builds?limit=1&sort_by=finished_at:desc", headers=headers)
    print(response.text)

#test_status(git_login_username, repository_name, ci_public_access_token)