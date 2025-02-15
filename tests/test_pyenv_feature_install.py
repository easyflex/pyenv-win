import subprocess


def test_check_pyenv_install_list(pyenv):
    result, stderr = pyenv.install('-l')
    assert stderr == ""
    assert "Mirror: https://www.python.org/ftp/python" in result
    assert "2.7.17-32" in result
    assert "2.7.17" in result
    assert "3.1.4-32" in result
    assert "3.1.4" in result
    assert "3.2.5-32" in result
    assert "3.2.5" in result
    assert "3.3.5-32" in result
    assert "3.3.5" in result
    assert "3.4.4-32" in result
    assert "3.4.4" in result
    assert "3.5.4-32" in result
    assert "3.5.4" in result
    assert "3.6.8-32" in result
    assert "3.6.8" in result
    assert "3.7.7-32" in result
    assert "3.7.7" in result
    assert "3.8.2-32" in result
    assert "3.8.2" in result
    assert "3.9.0-32" in result
    assert "3.9.0" in result
    assert "3.9.1-32" in result
    assert "3.9.1" in result


def test_check_pyenv_installation():
    # TODO: tracking the logs of installation and checking the folder
    pass
