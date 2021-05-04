import pytest
import io
import app
import name_generator



def test_get_user_name(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('bob'))
    result = app.get_user_name()
    assert result == 'bob'

def test_get_user_birth_month(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('March'))
    result = app.get_user_birth_month()
    assert result == 'March'

def test_get_user_animal(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('dragon'))
    result = app.get_user_animal()
    assert result == 'dragon'

@pytest.mark.parametrize('month, expected', [('March', 'Charmander'), ('December', 'Charizard')])
def test_handle_dragon_generator(month, expected):
    result = app.handle_dragon_generator(month)
    assert result == expected

@pytest.mark.parametrize('month, expected', [('March', 'Skipper'), ('December','Ice Cold') ])
def test_handle_penguin_generator(month, expected):
    result = app.handle_penguin_generator(month)
    assert result == expected
  
