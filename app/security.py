from passlib.context import CryptContext


class NoInstance(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can`t instance directly")


class Crypt(metaclass=NoInstances):
    crypt_ctx = CryptContext(schemes=["sha256_crypt"])

    @classmethod
    def verify(cls, plain_password: str, hashed_password: str) -> bool:
        return cls.crypt_ctx.verify(plain_password, hashed_password)

    @classmethod
    def hash(cls, password: str) -> str:
        return cls.crypt_ctx.hash(password)
