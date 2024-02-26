from abc import ABC, abstractmethod


class IAuthenticate(ABC):
    @abstractmethod
    def authenticate(self, credentials: str) -> None:
        pass


class IAuthorizer(ABC):
    @abstractmethod
    def authorize(self, user: str) -> None:
        pass


class BasicAuthenticator(IAuthenticate):
    def authenticate(self, credentials: str) -> None:
        print("Performing Basic Authentication")


class BasicAuthorizer(IAuthorizer):
    def authorize(self, user) -> None:
        print("Performing Basic Authorization")


class OAuthAuthenticator(IAuthenticate):
    def authenticate(self, credentials) -> None:
        print("Performing OAuth Authentication")


class OAuthAuthorizer(IAuthorizer):
    def authorize(self, user) -> None:
        print("Performing OAuth Authorization")


class IAuthFactory(ABC):
    @abstractmethod
    def create_authenticator(self) -> IAuthenticate:
        pass

    @abstractmethod
    def create_authorizer(self) -> IAuthorizer:
        pass


class BasicAuthFactory(IAuthFactory):
    def create_authenticator(self) -> BasicAuthenticator:
        return BasicAuthenticator()

    def create_authorizer(self) -> BasicAuthorizer:
        return BasicAuthorizer()


class OAuthFactory(IAuthFactory):
    def create_authenticator(self) -> OAuthAuthenticator:
        return OAuthAuthenticator()

    def create_authorizer(self) -> OAuthAuthorizer:
        return OAuthAuthorizer()


def authenticate_user(auth_factory: IAuthFactory, credentials: str) -> None:
    authenticator = auth_factory.create_authenticator()
    authenticator.authenticate(credentials)


def authorize_user(auth_factory: IAuthFactory, user: str) -> None:
    authorizer = auth_factory.create_authorizer()
    authorizer.authorize(user)


if __name__ == "__main__":
    basic_auth_factory = BasicAuthFactory()
    oauth_factory = OAuthFactory()

    # Authentication and authorization using Basic Auth
    authenticate_user(basic_auth_factory, "username:password")
    authorize_user(basic_auth_factory, "user")

    # Authentication and authorization using OAuth
    authenticate_user(oauth_factory, "oauth_token")
    authorize_user(oauth_factory, "user_id")
