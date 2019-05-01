from flask import jsonify


def template(data, code=500):
    return {'message': {'errors': {'body': data}}, 'status_code': code}


INVALID_FORM_DATA = template(['Invalid form data'], code=400)
USER_NOT_FOUND = template(['User not found'], code=404)
EMAIL_ALREADY_USED = template(['Email already used'], code=422)
UNKNOWN_ERROR = template([], code=500)

class InvalidUsage(Exception):
    status_code = 500

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_json(self):
        rv = self.message
        return jsonify(rv)

    @classmethod
    def invalid_form_data(cls):
        return cls(**INVALID_FORM_DATA)

    @classmethod
    def user_not_found(cls):
        return cls(**USER_NOT_FOUND)

    @classmethod
    def email_already_used(cls):
        return cls(**EMAIL_ALREADY_USED)

    @classmethod
    def unknown_error(cls):
        return cls(**UNKNOWN_ERROR)

