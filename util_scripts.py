import requests, os


def github_raw(module: str, repository: str, branch: str='master', path: str=os.getcwd()):
    '''Downloads modules from github raw'''
    base_url = f'https://raw.githubusercontent.com/gustav-gustav'
    filename = f'{module}.py'
    url = f'{base_url}/{repository}/{branch}/{filename}'
    with requests.get(url) as response:
        if response.ok:
            with open(filename, 'wb') as raw:
                raw.write(response.content)
        else:
            response.raise_for_status()

