import bcrypt

salt = bcrypt.gensalt()


def encrypt_password(password: str):
    return bcrypt.hashpw(password.encode(), salt)


def verify_password(password: str, hashed_password: str):
    return bcrypt.checkpw(password.encode(), hashed_password.encode())
