import os, sys
def print_error_details(error: Exception) -> None:
    """
    Print details of an error.

    The details printed are the class and cause of the error, the type of
    exception, the filename and line number where the exception occurred.

    :param error: The error to print details about.
    :type error: Exception
    """
    print(f'error class: {error.__class__} | error cause: {error.__cause__}')
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)