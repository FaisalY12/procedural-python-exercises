import pytest
import io
import app



def test_get_user_name(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('bob'))
    result = app.get_user_name()
    assert result == 'bob'

# @pytest.mark.parametrize('cat, expected, not_expected', [('basic', 'multiply', 'info'), ('advanced', 'rounding', 'add')])
# def test_get_option(cat, expected, not_expected, capsys, monkeypatch):
#     monkeypatch.setattr('sys.stdin', io.StringIO(expected))
#     app.get_option(cat)
#     out, err = capsys.readouterr()
#     assert expected in out
#     assert not_expected not in out

# def test_handle_basic(monkeypatch, capsys):
#     monkeypatch.setattr('sys.stdin', io.StringIO("2, 3"))
#     result = app.handle_basic('add')
#     assert result == 5.0

# def test_handle_advanced_info(monkeypatch, capsys):
#     monkeypatch.setattr('sys.stdin', io.StringIO("9"))
#     result = app.handle_advanced('info')
#     out, err = capsys.readouterr()
#     assert 'info' in out
#     assert '3' in result

# @pytest.mark.parametrize('input, expected', [
#     ('5.4 down', 5),
#     ('5.4 up', 6),
# ])
# def test_handle_advanced_rounding(input, expected, monkeypatch):
#     monkeypatch.setattr('sys.stdin', io.StringIO(input))
#     result = app.handle_advanced('rounding')
#     assert result == expected


# def test_app_error(monkeypatch, capsys):
#     monkeypatch.setattr('sys.stdin', io.StringIO('nonsense'))
#     app.run()
#     out, err = capsys.readouterr()
#     assert 'Terribly sorry' in out