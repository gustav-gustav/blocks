import requests, os, argparse
from decorators import ResponseTimer
requests.get = ResponseTimer(requests.get)

def github_raw(module: str, repository: str, user: str='gustav-gustav', branch: str='master', path: str=os.getcwd()):
    '''Downloads modules from github raw'''
    base_url = f'https://raw.githubusercontent.com/'
    filename = f'{module}.py'
    full_path = os.path.join(path, filename)
    url = f'{base_url}/{user}/{repository}/{branch}/{filename}'
    try:
        with requests.get(url) as response:
            if response.ok:
                with open(full_path, 'wb') as raw:
                    print(f'Creating {full_path}')
                    raw.write(response.content)
            else:
                response.raise_for_status()

    except requests.exceptions.HTTPError as httperr:
        if httperr.response.status_code == 404:
            print(f'No module named {module} in {repository}')
        else:
            raise httperr


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('module', action='store', type=str)
    parser.add_argument('repository', action='store', type=str)
    parser.add_argument('--user', '-u', dest='user', action='store', type=str, default='gustav-gustav')
    parser.add_argument('--branch', '-b', dest='branch', action='store', type=str, default='master')
    parser.add_argument('--path', '-p', dest='path', action='store', type=str, default=os.getcwd())
    args = parser.parse_args()
    github_raw(**vars(args))