import os
import requests

API_VERSION = 'v1'


def invoke_balena_supervisor_post(http_verb, endpoint):
    headers = {'Content-type': 'application/json'}
    supervisor_address = os.environ['BALENA_SUPERVISOR_ADDRESS']
    supervisor_api_key = os.environ['BALENA_SUPERVISOR_API_KEY']

    url = f"{supervisor_address}/{API_VERSION}/{endpoint}?apikey={supervisor_api_key}"
    return requests.request(http_verb, url, headers=headers)


def shutdown():
    response = invoke_balena_supervisor_post('POST', 'shutdown')

    if (response.status_code == 202):
        return response.json
    else:
        raise Exception(response.json)
