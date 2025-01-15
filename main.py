from GPTfFileUpdate import CodeAnalyzer
from GitHubGetFile import GitHubGetFile
from dotenv import load_dotenv
load_dotenv()
import os
class GitHubFileAnalyzer:
    def __init__(self, owner, repo, branch, file_path):
        self.github_get_file = GitHubGetFile(owner, repo, branch, file_path)
        self.folder_id = 'b1g53rg80vs5lefsnjco'
        self.auth = os.getenv('API_KEY')

    def analyze_file(self):
        file_content = self.github_get_file.get_file()
        if file_content:
            code_analyzer = CodeAnalyzer(file_content)
            code_analyzer.ask(self.folder_id, self.auth)


url = input("Please enter the GitHub file URL: ")
owner, repo, branch, file_path = url.replace('https://github.com/', '').replace('blob/', '').split('/', 3)
updatedFile = GitHubFileAnalyzer(owner, repo, branch, file_path)
updatedFile.analyze_file()
