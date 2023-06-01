from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    # Caso de sucesso
    with pytest.raises(TypeError) as erroKey:
        encrypt_message("menssagem", None)
    assert str(erroKey.value) == "tipo inválido para key"

    with pytest.raises(TypeError) as erroMessage:
        encrypt_message(None, 2)
    assert str(erroMessage.value) == "tipo inválido para message"

    assert encrypt_message("menssagem", 10) == "megassnem"

    assert encrypt_message("menssagem", 2) == "megassn_em"
