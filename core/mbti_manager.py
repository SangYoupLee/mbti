import json

class MBTIManager:
    def __init__(self, data_file='data/mbti_data.json'):
        with open(data_file, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def get_match(self, mbti):
        return self.data['match'].get(mbti, {})

    def get_strengths(self, mbti):
        return self.data['strengths'].get(mbti, [])

    def get_jobs(self, mbti):
        return self.data['jobs'].get(mbti, [])
