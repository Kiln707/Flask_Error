from werkzeug.exceptions import HTTPException

class PaymentRequired(HTTPException):
    code = 402
    description = 'A Payment is required to continue'

class ProxyAuthenticationRequired(HTTPException):
    code = 407
    description = 'Please authenticate with proxy'

class UnprocessableEntity(HTTPException):
    code = 422
    description = 'Unable to process request due to bad semantics'

class Locked(HTTPException):
    code = 423
    description = 'Requested resource is locked and unavailable.'

class UpgradeRequired(HTTPException):
    code = 426
    description = 'Please connect with an upgraded protocol.'

class NoResponse(HTTPException):
    code = 444
    description = 'Server provided no response.'

class UnavailableforLegalReasons(HTTPException):
    code = 451
    description = 'Access is denied to this resource, or to a set of resources that includes the requested resource, due to legal demands.'

class GatewayTimeout(HTTPException):
    code = 504
    description = 'Did not receive timely response from upstream server.'

class HTTPVersionNotSupported(HTTPException):
    code = 505
    description = 'The serverdoes not support the HTTP Protocol version used in the request.'

class VariantAlsoNegotiates(HTTPException):
    code = 506
    description = 'Transparent content negotiation for the request results in circular reference.'

class InsufficientStorage(HTTPException):
    code = 507
    description = 'The server does not have enough free space to process the request.'

class LoopDetected(HTTPException):
    code = 508
    description = 'The server has detected an infinite loop.'

class BandwidthLimitExceeded(HTTPException):
    code = 509
    description = 'The bandwidth limit has been exceeded.'

class NotExtended(HTTPException):
    code = 510
    description = 'Not enough information to fulfill the request.'

class NetworkAuthenticationRequired(HTTPException):
    code = 511
    description = 'Please authenticate to gain access.'
