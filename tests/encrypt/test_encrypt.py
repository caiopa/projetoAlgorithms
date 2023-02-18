from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    message = 'caiopereira'
    invalid_key = "1"
    invalid_message = 1

    assert encrypt_message(message, 4) == 'arierep_oiac'
    assert encrypt_message(message, 11) == 'arierepoiac'

    with pytest.raises(TypeError):
        encrypt_message(message, invalid_key)
    with pytest.raises(TypeError):
        encrypt_message(invalid_message, 4)