AUTH_LOGIN_SUCCESS_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": [
        "id", "username", "email", "firstName", "lastName",
        "gender", "image", "accessToken", "refreshToken"
    ],
    "properties": {
        "id": {"type": "integer"},
        "username": {"type": "string"},
        "email": {"type": "string"},
        "firstName": {"type": "string"},
        "lastName": {"type": "string"},
        "gender": {"type": "string"},
        "image": {"type": "string"},
        "accessToken": {"type": "string"},
        "refreshToken": {"type": "string"},
    },
    "additionalProperties": True
}

AUTH_ME_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": [
        "id", "username", "email", "firstName", "lastName", "gender", "image"
    ],
    "properties": {
        "id": {"type": "integer"},
        "username": {"type": "string"},
        "email": {"type": "string"},
        "firstName": {"type": "string"},
        "lastName": {"type": "string"},
        "gender": {"type": "string"},
        "image": {"type": "string"},
    },
    "additionalProperties": True
}

AUTH_REFRESH_SUCCESS_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": ["accessToken", "refreshToken"],
    "properties": {
        "accessToken": {"type": "string"},
        "refreshToken": {"type": "string"},
    },
    "additionalProperties": True
}

AUTH_ERROR_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "properties": {
        "message": {"type": "string"},
        "error": {"type": "string"},
        "status": {"type": ["integer", "string"]},
    },
    "additionalProperties": True
}
