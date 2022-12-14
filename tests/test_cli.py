import pytest
from pgbackup import cli

url = "postgres://bob@example.com:5432/db_one"

@pytest.fixture
def parser():
    return cli.create_parser()

def test_parser_without_driver(parser):
    """
    Without a specified driver the partser will exit
    """
    with pytest.raises(SystemExit):
        parser = cli.create_parser()
        parser.parse_args([url])


def test_parser_with_driver(parser):
    """
    The parser will exit if it receives a driver without a destination
    """
    parser = cli.create_parser()
    with pytest.raises(SystemExit):
        parser.parse_args([url, "--driver", "local"])

def test_parser_with_unknown_driver(parser):
    """
    The parser will exit if the driver name is unknown
    """
    parser = cli.create_parser()
    with pytest.raises(SystemExit):
        parser.parse_args([url, '--driver', 'azure', 'destination'])

def test_parser_with_known_drivers(parser):
    """
    The parser will not wxit if the driver name is known
    """
    parser = cli.create_parser()
    for driver in ['local', 's3']:
        assert parser.parse_args([url, '--driver', driver, 'destination'])

def test_parser_with_driver_and_destination(parser):
    """
    The parser will not exit if it receives a driver and destionation
    """
    parser = cli.create_parser()
    args = parser.parse_args([url, '--driver', 'local', '/some/path'])

    assert args.url == url
    assert args.driver == 'local'
    assert args.destination == '/some/path'
