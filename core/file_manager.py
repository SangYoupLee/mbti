from pathlib import Path


class FileManager:
    def __init__(self, path: str | None = None) -> None:
        """Manage user MBTI history.

        Parameters
        ----------
        path:
            Optional path to the history file. When ``None`` the path is
            resolved relative to the package location so it works
            regardless of the current working directory.
        """
        if path is None:
            base = Path(__file__).resolve().parents[1]
            self.path = base / "data" / "user_data.txt"
        else:
            self.path = Path(path)

    def save_user(self, mbti: str) -> None:
        """Append a user's MBTI type to the history file."""
        with self.path.open("a", encoding="utf-8") as f:
            f.write(mbti + "\n")

    def load_all(self) -> list[str]:
        """Return every stored MBTI type."""
        with self.path.open("r", encoding="utf-8") as f:
            return [line.strip() for line in f]
