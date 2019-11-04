from werkzeug.exceptions import HTTPException

class PaymentRequired(HTTPException):
    code = 402
    description = 'A Payment is required to continue'

class ProxyAuthenticationRequired(HTTPException):
    code = 407
    description = 'Please authenticate with proxy'

class EnhanceCalm():
    pass

class UnprocessableEntity():
    pass

class Locked():
    pass

class UpgradeRequired():
    pass

class NoResponse():
    pass

class RetryWith():
    pass

class BlockedByWindowsParentalControls():
    pass

class UnavailableforLegalReasons():
    pass

class 
