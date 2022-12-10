import pytest

from example import get_second_word


@pytest.mark.parametrize(
    "text, expected_word",
    [
        pytest.param("", None, id="empty text"),
        pytest.param("first", None, id="single word"),
        pytest.param("first second", "second", id="multiple words"),
        pytest.param("alpha beta", "beta", id="multiple words alternate"),
        pytest.param("first second third", "second", id="many words"),
    ],
)
def test_get_second_word(text: str, expected_word: str):
    returned_word = get_second_word(text)

    assert returned_word == expected_word


@pytest.mark.parametrize(
    "text, expected_word",
    [
        pytest.param("", None, id="empty text"),
        pytest.param("first", None, id="single word"),
        pytest.param(f"first {(second := 'second')}", second, id="multiple words"),
        pytest.param(
            f"alpha {(second := 'beta')}", second, id="multiple words alternate"
        ),
        pytest.param(f"first {(second := 'second')} third", second, id="many words"),
    ],
)
def test_get_second_word_walrus(text: str, expected_word: str):
    returned_word = get_second_word(text)

    assert returned_word == expected_word


@pytest.mark.parametrize(
    "text, expected_word",
    [
        pytest.param("", None, id="empty text"),
        pytest.param("first", None, id="single word"),
        pytest.param(f"first {(second := 'second')}", second, id="multiple words"),
        pytest.param(
            f"alpha {(second := 'beta')}", second, id="multiple words alternate"
        ),
        pytest.param(f"first {(second_ := 'second')} third", second, id="many words"),
    ],
)
def test_get_second_word_walrus_mistake(text: str, expected_word: str):
    returned_word = get_second_word(text)

    assert returned_word == expected_word


# pylint: disable=unused-variable,undefined-variable,too-many-locals
@pytest.mark.parametrize(
    "text, expected_word",
    [
        pytest.param("", None, id="empty text"),
        pytest.param("first", None, id="single word"),
        pytest.param(f"first {(second := 'second')}", second, id="multiple words"),
        pytest.param(
            f"alpha {(second := 'beta')}", second, id="multiple words alternate"
        ),
        pytest.param(f"first {(second := 'second')} third", second, id="many words"),
    ],
)
# pylint: enable=unused-variable,undefined-variable,too-many-locals
def test_get_second_word_walrus_pylint(text: str, expected_word: str):
    returned_word = get_second_word(text)

    assert returned_word == expected_word


@pytest.mark.parametrize(
    "text, expected_word",
    [
        pytest.param("", None, id="empty text"),
        pytest.param("first", None, id="single word"),
        pytest.param(text := "first second", text.split()[1], id="multiple words"),
        pytest.param(
            text := "alpha beta", text.split()[1], id="multiple words alternate"
        ),
        pytest.param(text := "first second third", text.split()[1], id="many words"),
    ],
)
def test_get_second_word_walrus_too_far(text: str, expected_word: str):
    returned_word = get_second_word(text)

    assert returned_word == expected_word
