import requests
import base64
class GitHubGetFile:
    def __init__(self, owner, repo, branch, file_path):
        self.owner = owner # nickname на github
        self.repo = repo # название репозитория
        self.branch = branch # название ветки
        self.file_path = file_path # путь к файлу
        self.url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}?ref={branch}"

    def get_file(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            file_info = response.json()
            file_content = base64.b64decode(file_info['content']).decode('utf-8')
            return file_content
        else:
            print(f"Не удалось загрузить файл. Код ошибки: {response.status_code}")
            return None
