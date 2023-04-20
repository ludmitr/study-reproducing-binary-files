# https://academy.masterschool.com/ns/books/published/swe/WritingFiles/7-HandlingBinaryFiles.html
def main():
    create_copy("baseball.jpg", "baseball-copy.jpg")


def create_copy(original_file_path: str, copy_file_path: str):
    """created copy of original_file_path in copy_file_path """
    with open(original_file_path, "rb") as file:
        original_data = file.read()



    with open(copy_file_path, "wb") as file:
        file.write(original_data)



if __name__ == '__main__':
    main()