class User:
    def __init__(self, mbti=None):
        self.mbti = mbti.upper() if mbti else None

    def set_mbti(self, mbti_str):
        self.mbti = mbti_str.upper()