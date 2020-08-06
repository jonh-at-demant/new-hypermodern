import click.testing

from new_hypermodern import console


def test_main_succeeds():
    """Test whether console main exits with 0"""
    runner = click.testing.CliRunner()
    result = runner.invoke(console.main)
    assert result.exit_code == 0
