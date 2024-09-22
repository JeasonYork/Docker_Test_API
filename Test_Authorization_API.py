import os
import requests

#os.environ['LOG'] = '1'

def test_authorization_api(api_address, api_port, api_username, api_pwd, version):
    endpoint = f'/v{version}/sentiment'
    sentence = "Test sentence"
    r = requests.get(
        url=f'http://{api_address}:{api_port}{endpoint}',
        params={
            'username': api_username,
            'password': api_pwd,
            'sentence': sentence
        }
    )

    status_code = r.status_code
    test_status = 'SUCCESS' if status_code == 200 else 'FAILURE'

    output = f'''
    ============================
        Authorization test
    ============================

    request done at "{endpoint}"
    | username="{api_username}"
    | password="{api_pwd}"
    | sentence="{sentence}"

    expected result = 200
    actual result = {status_code}

    ==>  {test_status}

    '''
    print(output)
    log_path = '/logs/api_test.log'
    if os.environ.get('LOG') == '1':
        with open(log_path, 'a') as file:
            file.write(output)

if __name__ == "__main__":
    api_address = os.getenv('API_ADDRESS', 'localhost')
    api_port = os.getenv('API_PORT', 8000)

    test_authorization_api(api_address, api_port, 'alice', 'wonderland', 1)
    test_authorization_api(api_address, api_port, 'alice', 'wonderland', 2)
    test_authorization_api(api_address, api_port, 'bob', 'builder', 1)
    test_authorization_api(api_address, api_port, 'bob', 'builder', 2)
