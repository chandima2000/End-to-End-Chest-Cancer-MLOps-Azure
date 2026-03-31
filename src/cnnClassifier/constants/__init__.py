from pathlib import Path

# Resolve paths relative to the project root so config is found regardless of CWD
PROJECT_ROOT = Path(__file__).resolve().parents[3]
CONFIG_FILE_PATH = PROJECT_ROOT / "config" / "config.yaml"
PARAMS_FILE_PATH = PROJECT_ROOT / "params.yaml"