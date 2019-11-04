from werkzeug.exceptions import HTTPException

class PaymentRequired(HTTPException):
    code = 400
    description = ''
