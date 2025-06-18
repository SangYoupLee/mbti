import json
from pathlib import Path

class MBTIManager:
    def __init__(self, data_file: str | None = None) -> None:
        """Load MBTI matching data from ``data/mbti_data.json``.

        Parameters
        ----------
        data_file:
            Optional path to the json file. When ``None`` the path is
            resolved relative to this package so the class works
            regardless of the current working directory.
        """
        if data_file is None:
            base = Path(__file__).resolve().parents[1]
            data_file = base / "data" / "mbti_data.json"
        else:
            data_file = Path(data_file)

        with data_file.open("r", encoding="utf-8") as f:
            self.data = json.load(f)

    def get_match(self, mbti):
        return self.data['match'].get(mbti, {})

    def get_strengths(self, mbti):
        return self.data['strengths'].get(mbti, [])

    def get_jobs(self, mbti):
        return self.data['jobs'].get(mbti, [])
