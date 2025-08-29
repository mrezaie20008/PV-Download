from pathlib import Path
from pickle import load

def setter():
    def getter() -> dict:
        file = open(Path(__file__).parent / ".bin", "rb")
        
        return load(file)

    data: dict = getter()

    for k, v in data.items():
        globals()[k] = v

setter()

