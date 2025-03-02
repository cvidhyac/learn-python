from pathlib import Path


class FilesExample:
    """
    Example class demonstrating usage of file functions in python
    """

    def __init__(self, file_path: str):
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

    def count_words_in_file(self) -> int:
        words = self._read_contents().split()
        return len(words)

    def write_text_to_file(self, contents: str) -> None:
        self._as_path.write_text(contents)
        print("File Write Successful!")


if __name__ == "__main__":
    filesObj = FilesExample('../text_files/pi_digits.txt')
    filesObj.print_file_as_lines()
    print(f"Value Of Pi: {filesObj.concat_lines_to_one_line()}")

    another_file = FilesExample("../text_files/lorem_ipsum.txt")
    num_of_words = another_file.count_words_in_file()
    print(f"Number of words in this text file is {num_of_words}")

    story_of_my_life = """
    The story of my life
    
    
    line1
    ...
    line 1000
    ----
    line 100_000_000
    """

    data = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
Fusce ac turpis quis ligula lacinia aliquet. Mauris ipsum. Nulla metus metus, ullamcorper vel, tincidunt sed, euismod in, nibh. Quisque volutpat condimentum velit. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nam nec ante. 
Vestibulum sapien. Proin quam. Etiam ultrices. Suspendisse in justo eu magna luctus suscipit. Sed lectus. Integer euismod lacus luctus magna.  Integer id quam. Morbi mi. Quisque nisl felis, venenatis tristique, dignissim in, ultrices sit amet, augue. Proin sodales libero eget ante.
    """
    write_lorem_obj = FilesExample("../text_files/lorem_ipsum_latin.txt")
    write_story_obj = FilesExample("../text_files/story-of-my-life.txt")
    write_lorem_obj.write_text_to_file(data)
    write_story_obj.write_text_to_file(story_of_my_life)
