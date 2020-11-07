import re, pyperclip


# ! python3

# Create regex object for phone numbers
def regex_phone_numbers(text_pattern):
    phone_regex = re.compile(
        r'''
          ((\d\d\d)|(\(\d\d\d\)))?
          (\s|-)
          (\d\d\d-\d\d\d\d)
          (((ext(\.)?\s)|x)              # extension word part ext. or x
            (\d{2,5}))?                     # extension part 00000
          ''', re.VERBOSE)
    phone_list = []
    for match_found in re.finditer(phone_regex, text_pattern):
        phone_list.append(match_found.group())
    return phone_list


# Create regex object for email addresses
def regex_email_address(text_pattern):
    email_regex = re.compile(r'''
        [a-zA-Z0-9._!#+]+                     #First_name/Last_name/email handler
        @                                     # Email separator @ character
        [a-zA-Z0-9._!#+]+                     # Domain provider
        ''', re.VERBOSE)
    email_list = []
    for match_found in re.finditer(email_regex, text_pattern):
        email_list.append(match_found.group())
    return email_list


def join_results(email_list, phone_list):
    final_list = []
    if len(email_list) != len(phone_list):
      print("Some emails do not have corresponding phone numbers")
    else:
        print("The length of email list is : " + str(len(email_list)))
        for i in range(len(email_list)):
            final_list.append(email_list[i] + " " + phone_list[i])
    print(final_list)
    return final_list



# Do a ctrl + c and copy the contents of the file email_phone_numbers.txt
# or the PDF directory file examplePhoneEmailDirectory.pdf
text_pattern = pyperclip.paste()
phone_extract = regex_phone_numbers(text_pattern)
print(phone_extract)
email_extract = regex_email_address(text_pattern)
print(email_extract)

## At this point respective index corresponding user and phone number
## are organized by index : [0] 123-123-1234, [0] userA@email.com
final_list = join_results(email_extract, phone_extract)

## Now the output is ready to copy to clip board
## Note - pyperclip can only copy str, int or bool, a.k.a primitive types
pyperclip.copy(str(final_list))

