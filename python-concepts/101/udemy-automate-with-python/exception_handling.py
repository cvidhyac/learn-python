# try-except equivalent to try-catch in java
# raise equivalent to throws keyword in java
# Traceback.format is equivalent to printStackTrace in java but can be used
# for writing the stack trace to a file

# All exceptions have a parent BaseException class, when except is not qualified
# it defaults to any exception extending from base exception (similar concept to
# Java). We should specify one or more qualified exception to make the handling
# meaningful.

# Finally clause similar to java, executes end of the program irrespective of
# exception and exits the method

# ------------
# Logging Notes
# Add logging instead of print - an extra logging level CRITICAL
# Use %s similar to parameterize log params

import logging
import traceback



def raise_exception_if_file_is_not_present():
    file_name = "./non_existent_file"
    try:
      open(file_name, "r")
    except FileNotFoundError:
        logging.critical(
          '''Exception caught trying to open a non existent file : %s''',
          file_name)
        raise Exception("File is not present : " + traceback.format_exc())
    finally:
        logging.info("program execution complete!")


def demo():
    raise_exception_if_file_is_not_present()


demo()
