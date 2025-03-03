import string_basics
import pytest

def test_formatted_name():
    with pytest.raises(ValueError, match=r"First name is empty"):
        string_basics.get_formatted_name('', "Doe")

    with pytest.raises(ValueError, match=r"First name is empty"):
        string_basics.get_formatted_name("    ", "Doe")


    with pytest.raises(ValueError, match=r"Last name is empty"):
        string_basics.get_formatted_name('John', "")

    with pytest.raises(ValueError, match=r"Last name is empty"):
        string_basics.get_formatted_name("John", "   ")

    assert string_basics.get_formatted_name("john", "doe") == "John Doe"