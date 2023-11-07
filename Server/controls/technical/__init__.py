import jwt, time
from functools import wraps
from flask import request
from dotenv import load_dotenv
import os
from exceptions import InvalidRole, TokenExpired

class TechnicalControls:
    def is_role(required_roles):
        def decorator(view_func):
            @wraps(view_func)
            def roleCheck(*args, **kwargs):
                load_dotenv()
                auth_header = request.headers.get('Authorization')
                if auth_header and auth_header.startswith('Bearer '):
                    token = auth_header[len('Bearer '):]
                    try:
                        jwt_decoded = jwt.decode(token.encode('utf-8'), os.getenv('JWT_SECRET'), algorithms=[os.getenv('JWT_ALGO')])
                        user_role = jwt_decoded.get('role')
                        if 'exp' in jwt_decoded and jwt_decoded['exp'] < time.time():
                            raise TokenExpired("Token has expired")

                        if user_role not in [role.value for role in required_roles]:
                            raise InvalidRole("Invalid permission")
                    except jwt.ExpiredSignatureError:
                        return 'Token has expired', 401
                    except (jwt.DecodeError, InvalidRole):
                        return 'Invalid token', 401
                else:
                    return 'Unauthorized', 401
                return view_func(*args, **kwargs)
            return roleCheck
        return decorator
