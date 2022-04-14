class Constants:
    """Hashing constants"""
    RANDOM_SALT_LENGTH = 32
    ITERATIONS_OF_SHA256 = 100000
    ENCODE_STYLE = 'sha256'
    PASSWORD_ENCODE_STYLE = 'utf-8'

    """Logger name"""
    LOGGERNAME = "central_logger.txt"

    """Server response codes"""
    SERVER_RESPONSE_OK = 0
    SERVER_RESPONSE_EXISTING_USER = 3
    SERVER_RESPONSE_NO_USER_FOUNDER = 1
    SERVER_RESPONSE_INVALID_PASSWORD = 2
    SERVER_RESPONSE_USER_ALL_READY_LOGGED_OUT = 8
    SERVER_RESPONSE_INVALID_AUTHENTICATION_HEADER = 9

    """Custom key inclusion response code"""
    CUSTOMERRORMESSAGERESPONSECODE = 10

    """password lifetime in days"""
    PASSWORDLIFETIME = 1

    """Header auth for logon"""
    AUTHENTICATIONHEADERFORLOGON = "4bbe7b23-1b5e-44f6-a9c0-f7c9fe0b234f"


    """Database"""
    databaseuser = "itibe"
    databasepassword = "chemboy"
    databasehost = "etherealmind.ddns.net"
    DATABASEURL ="mysql+pymysql://" + databaseuser + ":" + databasepassword + "@" + databasehost + "/coin"
