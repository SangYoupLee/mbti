import tkinter as tk
from mbti.core.user import User
from mbti.core.mbti_manager import MBTIManager
from mbti.core.file_manager import FileManager

class MBTIGUI:
    def __init__(self):
        self.user = User()
        self.manager = MBTIManager()
        self.file = FileManager()

        self.root = tk.Tk()
        self.root.title("MBTI MatchMate")

        self.build_ui()

    def build_ui(self):
        tk.Label(self.root, text="당신의 MBTI를 입력해주세요 (예: INFP)").pack()
        self.entry = tk.Entry(self.root)
        self.entry.pack()

        tk.Button(self.root, text="결과 보기", command=self.show_result).pack()
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def show_result(self):
        mbti = self.entry.get()
        self.user.set_mbti(mbti)
        self.file.save_user(mbti)

        match = self.manager.get_match(mbti)
        if match:
            best = max(match, key=match.get)
            self.result_label.config(text=f"가장 잘 맞는 MBTI는 {best} ({match[best]}%)")
        else:
            self.result_label.config(text="유효한 MBTI가 아니거나 데이터가 없습니다.")

    def run(self):
        self.root.mainloop()
