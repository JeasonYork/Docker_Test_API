import os
import requests

#os.environ['LOG'] = '1'

def test_content_api(api_address, api_port, api_username, api_pwd):
    sentences = [
        ("life is beautiful", "positive"),
        ("that sucks", "negative")
    ]

    for sentence, expected_score in sentences:
        for version in [1, 2]:
            endpoint = f'/v{version}/sentiment'
            r = requests.get(
                url=f'http://{api_address}:{api_port}{endpoint}',
                params={
                    'username': api_username,
                    'password': api_pwd,
                    'sentence': sentence
                }
            )

            status_code = r.status_code
            response_data = r.json()
            score = response_data.get('score')

            #print('response_data:',response_data)
            #print('score:',score)
            if score is None:
                test_status = 'FAILURE'
            else:
                sentiment = 'positive' if score > 0 else 'negative'
                test_status = 'SUCCESS' if sentiment == expected_score else 'FAILURE'

            output = f'''
            ============================
                Content test
            ============================

            request done at "{endpoint}"
            | username="{api_username}"
            | password="{api_pwd}"
            | sentence="{sentence}"

            expected sentiment = {expected_score}
            actual sentiment = {sentiment if score is not None else 'unknown'}

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

    test_content_api(api_address, api_port, 'alice', 'wonderland')
