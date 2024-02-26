import pytest
from creational.abstract_factory.auth import (
    BasicAuthFactory,
    OAuthFactory,
    IAuthFactory,
    IAuthenticate,
    IAuthorizer,
)
from creational.abstract_factory.auth import authenticate_user, authorize_user


class MockAuthFactory(IAuthFactory):
    def create_authenticator(self) -> IAuthenticate:
        return None

    def create_authorizer(self) -> IAuthorizer:
        return None


def test_basic_authentication(capsys):
    basic_auth_factory = BasicAuthFactory()
    authenticate_user(basic_auth_factory, "username:password")
    captured = capsys.readouterr()
    assert captured.out == "Performing Basic Authentication\n"


def test_basic_authorization(capsys):
    basic_auth_factory = BasicAuthFactory()
    authorize_user(basic_auth_factory, "user")
    captured = capsys.readouterr()
    assert captured.out == "Performing Basic Authorization\n"


def test_oauth_authentication(capsys):
    oauth_factory = OAuthFactory()
    authenticate_user(oauth_factory, "oauth_token")
    captured = capsys.readouterr()
    assert captured.out == "Performing OAuth Authentication\n"


def test_oauth_authorization(capsys):
    oauth_factory = OAuthFactory()
    authorize_user(oauth_factory, "user_id")
    captured = capsys.readouterr()
    assert captured.out == "Performing OAuth Authorization\n"


# Test invalid factory
def test_invalid_factory():
    with pytest.raises(AttributeError):
        invalid_factory = MockAuthFactory()
        authenticate_user(invalid_factory, "credentials")


if __name__ == "__main__":
    pytest.main()
