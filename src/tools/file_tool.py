import os

class FileTool:
    @staticmethod
    def write_to_file(path: str, content: str):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            f.write(content)

    @staticmethod
    def read_file(path: str) -> str:
        with open(path, 'r') as f:
            return f.read()
