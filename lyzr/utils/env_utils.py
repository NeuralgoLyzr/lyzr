from pathlib import Path
from dotenv import load_dotenv

def find_and_load_dotenv(start_path: Path) -> Path:
    current_path = start_path
    while current_path != Path('/'):
        dotenv_path = current_path / '.env'
        if dotenv_path.exists(): 
            load_dotenv(dotenv_path) 
        current_path = current_path.parent
    raise OSError('Could not find a .env file.')