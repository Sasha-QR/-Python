import pytest
from string_utils import StringUtils


@pytest.fixture
def utils():
    return StringUtils()


# =========================================================
# ТЕСТЫ ДЛЯ capitalize
# =========================================================

# ----------------
# Позитивные
# ----------------

def test_capitalize_regular_text(utils):
    assert utils.capitalize("Тест") == "Тест"


def test_capitalize_numbers_string(utils):
    assert utils.capitalize("123") == "123"


def test_capitalize_string_with_spaces(utils):
    assert utils.capitalize("04 апреля 2023") == "04 апреля 2023"


# ----------------
# Негативные
# ----------------

def test_capitalize_empty_string(utils):
    assert utils.capitalize("") == ""


def test_capitalize_single_space(utils):
    assert utils.capitalize(" ") == " "


def test_capitalize_none(utils):
    with pytest.raises(AttributeError):
        utils.capitalize(None)


def test_capitalize_list(utils):
    with pytest.raises(AttributeError):
        utils.capitalize([])


# =========================================================
# ТЕСТЫ ДЛЯ trim
# =========================================================

# ----------------
# Позитивные
# ----------------

def test_trim_regular_text(utils):
    assert utils.trim("   Тест") == "Тест"


def test_trim_numbers_string(utils):
    assert utils.trim("   123") == "123"


def test_trim_string_with_spaces_inside(utils):
    assert utils.trim("   04 апреля 2023") == "04 апреля 2023"


# ----------------
# Негативные
# ----------------

def test_trim_empty_string(utils):
    assert utils.trim("") == ""


def test_trim_single_space(utils):
    assert utils.trim(" ") == ""


def test_trim_none(utils):
    with pytest.raises(AttributeError):
        utils.trim(None)


def test_trim_list(utils):
    with pytest.raises(AttributeError):
        utils.trim([])


# =========================================================
# ТЕСТЫ ДЛЯ contains
# =========================================================

# ----------------
# Позитивные
# ----------------

def test_contains_regular_text(utils):
    assert utils.contains("Тест", "е") is True


def test_contains_numbers_string(utils):
    assert utils.contains("123", "2") is True


def test_contains_string_with_spaces(utils):
    assert utils.contains("04 апреля 2023", "апреля") is True


# ----------------
# Негативные
# ----------------

def test_contains_empty_string(utils):
    assert utils.contains("", "а") is False


def test_contains_single_space(utils):
    assert utils.contains(" ", " ") is True


def test_contains_none(utils):
    with pytest.raises(AttributeError):
        utils.contains(None, "a")


def test_contains_symbol_none(utils):
    with pytest.raises(TypeError):
        utils.contains("Тест", None)


def test_contains_list(utils):
    with pytest.raises(AttributeError):
        utils.contains([], "a")


# =========================================================
# ТЕСТЫ ДЛЯ delete_symbol
# =========================================================

# ----------------
# Позитивные
# ----------------

def test_delete_symbol_regular_text(utils):
    assert utils.delete_symbol("Тест", "е") == "Тст"


def test_delete_symbol_numbers_string(utils):
    assert utils.delete_symbol("123123", "1") == "2323"


def test_delete_symbol_string_with_spaces(utils):
    assert utils.delete_symbol("04 апреля 2023", " ") == "04апреля2023"


# ----------------
# Негативные
# ----------------

def test_delete_symbol_empty_string(utils):
    assert utils.delete_symbol("", "a") == ""


def test_delete_symbol_single_space(utils):
    assert utils.delete_symbol(" ", " ") == ""


def test_delete_symbol_none(utils):
    with pytest.raises(AttributeError):
        utils.delete_symbol(None, "a")


def test_delete_symbol_symbol_none(utils):
    with pytest.raises(TypeError):
        utils.delete_symbol("Тест", None)


def test_delete_symbol_list(utils):
    with pytest.raises(AttributeError):
        utils.delete_symbol([], "a")
