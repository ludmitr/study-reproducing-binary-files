# https://academy.masterschool.com/ns/books/published/swe/WritingFiles/7-HandlingBinaryFiles.html
def main():
    create_copy("baseball.jpg", "baseball-copy.jpg")
    create_double_song("sample.mp3", "sample-twice.mp3")
    create_first_n_char("baseball.jpg", "baseball-part.jpg", 30000)


def create_copy(original_file_path: str, copy_file_path: str):
    """created copy of original_file_path in copy_file_path """
    with open(original_file_path, "rb") as file:
        original_data = file.read()
    with open(copy_file_path, "wb") as file:
        file.write(original_data)


def create_double_song(original_file_path: str, copy_file_path: str):
    """creating 2 repeated mp3 in one
    from original_file_path to copy_file_path
    """
    with open(original_file_path, "rb") as file:
        original_data = file.read()
    with open(copy_file_path, "wb") as file:
        file.write(original_data + original_data)


def create_first_n_char(original_file_path: str, copy_file_path: str, first_n_chars: int):
    """Create a copy of original_file_path under the name copy_file_path
     that contains only the first_n_chars “characters”"""
    with open(original_file_path, "rb") as file:
        original_data = file.read()
    with open(copy_file_path, "wb") as file:
        file.write(original_data[:first_n_chars])




if __name__ == '__main__':
    main()