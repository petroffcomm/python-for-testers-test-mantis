
from datagen.utils import rnd_name_string


def test_sign_up_new_account(app):
    username = rnd_name_string("user_", 10)
    password = "test"
    email = username + "@localhost"

    app.james.ensure_user_exists(username, password)
    app.mantis_signup.new_user(username, email, password)

    assert app.mantis_soap_api.can_login(username, password)
