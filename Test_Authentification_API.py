import os
import requests

#os.environ['LOG'] = '1'

def test_authentication_api(api_address, api_port, api_username, api_pwd):
    r = requests.get(
        url=f'http://{api_address}:{api_port}/permissions',
        params={
            'username': api_username,
            'password': api_pwd
        }
    )

    status_code = r.status_code
    test_status = 'SUCCESS' if status_code == 200 else 'FAILURE'

    output = f'''
    ============================
        Authentication test
    ============================

    request done at "/permissions"
    | username="{api_username}"
    | password="{api_pwd}"

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

    credentials = [
        ('alice', 'wonderland'),
        ('bob', 'builder'),
        ('clementine', 'mandarine')
    ]

    for username, password in credentials:
        test_authentication_api(api_address, api_port, username, password)

