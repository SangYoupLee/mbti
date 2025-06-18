class FileManager:
    def __init__(self, path='data/user_data.txt'):
        self.path = path

    def save_user(self, mbti):
        with open(self.path, 'a') as f:
            f.write(mbti + '\\n')

    def load_all(self):
        with open(self.path, 'r') as f:
            return [line.strip() for line in f]
