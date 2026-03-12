import subprocess
import sys

class ExecutionTool:
    @staticmethod
    def run_python_code(code: str) -> str:
        try:
            result = subprocess.run(
                [sys.executable, "-c", code],
                capture_output=True,
                text=True,
                timeout=5
            )
            return result.stdout if result.returncode == 0 else result.stderr
        except Exception as e:
            return str(e)
