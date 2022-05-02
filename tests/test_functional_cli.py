from typer.testing import CliRunner
from cli import main

runner = CliRunner()


def test_add_anime():
    result = runner.invoke(main, ["add", "Cowboy Bebop", "Sunrise",
                                  "--genres=sci-fi, action", "--episodes=26",
                                  "--score=8.7"])
    assert result.exit_code == 0
    assert "Anime added to database" in result.stdout
