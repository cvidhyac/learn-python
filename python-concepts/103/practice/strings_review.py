
def format_money():
    money_value = 50000
    formatted_money = f"{money_value:,.2f}"
    print(formatted_money)

def join_with_comma():
    str_with_comma = ",".join([str(num) for num in range(10)])
    print(str_with_comma)


def reverse_name_with_format():
    name = "John Doe"
    name = ", ".join(reversed(name.split()))
    print(name)


def count_occurrences():
    """
    Count is used for counting occurrences of a substring in a string
    When index is not specified, it counts from 0th index, otherwise starts from the specified start and or end index
    :return:
    """
    sentence = "to be or not to be that is the question"
    print(f"Count Occurrences of the word 'to': {sentence.count("to")}")
    print(f"Count Occurrences of the word 'to' after 10th index: {sentence.count("to",  10)}")
    print(f"Count Occurrences of the word 'to' after 10th index: {sentence.count("to", 10, 11)}")

def replace_strings():
    values = "1\t2\t3\t4\t5\t6\t7\t8\t9"
    a_new_str = values.replace("\t", "-->")
    print(f"Original string: {values}, replaced string: {a_new_str}")

def practice_ex():
    sentence = "to be or not to be that is the question"
    as_array = sentence.split(" ")
    for word in as_array:
        if word.startswith("t"):
            print(word, end=' ')
    print(end="\n")

def partitioning_a_string():
    """
    Partitions a string into substrings based on a specific substring or set of characters. The response of
    partition is a tuple and can be unpacked in same operation. This is a useful technique to split urls
    :return:
    """
    student_grades = "Alex: 88, 90, 92"
    student_name, separator, grades = student_grades.partition(": ")
    print(f"Student grades after partition: {grades}")

    url_partitions = "https://www.textbook.com/pdf/documents/chapter01.html"
    host, separator, rest_of_url = url_partitions.partition("://")
    print(f"Host: {host}, separator: {separator}, rest_of_url: {rest_of_url}")

    rest_of_url, separator, chapter_name = rest_of_url.rpartition("/")
    print(chapter_name)


def practice_ex_one():
    url = "https://www.deitel.com/books/PyCDS/table_of_contents.html"
    host, separator, rest_of_url = url.partition("://")
    print(f"Host: {host}, separator: {separator}, rest_of_url: {rest_of_url}")
    host_name_with_path, separator, page_name = rest_of_url.rpartition("/")
    print(f"Host_name: {host_name_with_path}, separator: {separator}, path: {page_name}")
    host_name, separator, path = host_name_with_path.partition("/")
    print(f"Host_name: {host_name}, separator: {separator}, path: {path}")

def character_testing_methods():
    a_string = "abcdefg6768"
    print(f"Is Alphanumeric: {a_string.isalnum()}")
    print(f"Is only alphabets: {a_string.isalpha()}")
    print(f"Is Digits: {a_string.isdigit()}")
    print(f"Is lower cased? : {a_string.islower()}")


if __name__ == '__main__':
    join_with_comma()
    reverse_name_with_format()
    count_occurrences()
    practice_ex()
    replace_strings()
    partitioning_a_string()
    practice_ex_one()
    character_testing_methods()
    format_money()