from dataclasses import dataclass
import string


@dataclass
class Dataingestionartifact:
    trained_file_path: str
    test_file_path: str
