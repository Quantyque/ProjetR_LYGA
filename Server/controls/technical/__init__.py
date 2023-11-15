import jwt, time
from functools import wraps
from flask import request
from dotenv import load_dotenv
import os
from exceptions import InvalidRole, TokenExpired, InvalidCredentials
from constants import AUTH_SYSTEM

class TechnicalControls:
    def is_role(required_roles):
        """
        Décorateur pour vérifier les permissions d'un utilisateur.

        Args:
            required_roles (list): Les permissions requises.

        Returns:
            function: La fonction décorée.

        Raises:
            InvalidRole: Si l'utilisateur n'a pas les permissions requises.
            TokenExpired: Si le token a expiré.
            InvalidToken: Si le token est invalide.
        """
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
    
    def check_is_user(token: str, id: int):
        """
        Vérifie que l'utilisateur est bien l'utilisateur dont l'id est passé en paramètre. Pas de vérification si l'utilisateur est un admin.

        Args:
            token (str): Le token de connexion.
            id (int): L'id de l'utilisateur.

        Raises:
            InvalidToken: Si le token est invalide.
            InvalidCredentials: Si l'utilisateur n'est pas le bon.
        """

        if AUTH_SYSTEM == True:
        
            load_dotenv()
            auth_header = token

            if auth_header and auth_header.startswith('Bearer '):

                token = auth_header[len('Bearer '):]

                try:

                    jwt_decoded = jwt.decode(token.encode('utf-8'), os.getenv('JWT_SECRET'), algorithms=[os.getenv('JWT_ALGO')])
                    user_id: int = jwt_decoded.get('id')
                    user_role: int = jwt_decoded.get('role')

                    if user_role != 0 and user_id != id:
                        raise InvalidCredentials("Invalid credentials")
                    
                except jwt.ExpiredSignatureError:

                    raise TokenExpired("Token has expired")
                
                except (jwt.DecodeError, InvalidCredentials):

                    raise InvalidCredentials("Invalid credentials")
                
            else:
                raise InvalidCredentials("Invalid credentials")
            
        else:
            pass
