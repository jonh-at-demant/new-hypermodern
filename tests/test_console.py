import click.testing
import pytest

from new_hypermodern import console


@pytest.fixture
def runner():
    return click.testing.CliRunner()

def test_main_succeeds(runner):
    """Test whether console main exits with 0"""
    result = runner.invoke(console.main)
    assert result.exit_code == 0
