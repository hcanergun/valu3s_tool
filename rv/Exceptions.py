"""
::: SAMPLE USAGE :::

class SalaryNotInRangeError(Exception):
    '''Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    '''

    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)


salary = int(input("Enter salary amount: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)

"""


# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class GetExecutableAuth(Error):
    """Exception raised when the generator can't get executable authentication"""
    pass


class ConvertYAML2MonitorPy(Error):
    """Exception raised when the .yaml file can't convert"""
    pass


class LinkMonitor2ROSWs(Error):
    """Exception raised when the monitor folder linking to Ros workspace"""
