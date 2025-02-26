import bcrypt


async def hash_password(password_user: str) -> bytes:
    salt = bcrypt.gensalt()
    password_bytes = password_user.encode()
    return bcrypt.hashpw(password_bytes, salt)
