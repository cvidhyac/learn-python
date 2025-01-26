from pathlib import Path

class FilesExample:
    """
    Example class demonstrating usage of file functions in python
    """

    def __init__(self, file_path:str):
        self.file_path = file_path
        self._as_path = Path(file_path)


    def _read_contents(self):
        return self._as_path.read_text()

    def print_file_as_lines(self):
        lines = self._read_contents().splitlines()
        for line in lines:
            print(line.strip())

    def concat_lines_to_one_line(self) -> str:
        lines = self._read_contents().splitlines()
        as_line_str = ""
        for line in lines:
            as_line_str += line.strip()
        return as_line_str

if __name__ == "__main__":
    filesObj = FilesExample('../text_files/pi_digits.txt')
    filesObj.print_file_as_lines()
    print(f"Value Of Pi: {filesObj.concat_lines_to_one_line()}")
