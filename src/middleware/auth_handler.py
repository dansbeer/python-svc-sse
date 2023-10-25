import time
import traceback
import jwt

JWT_SECRET = ""
JWT_ALGORITHM = "HS256"

def token_response(token: str):
    return {
        "access_token": token
    }

def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["exp"] >= time.time() else None
    except Exception as e:
        traceback.print_exc(e)
        return None
