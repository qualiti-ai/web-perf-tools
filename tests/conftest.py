import pytest
from pylenium.driver import Pylenium


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="",
        help="The URL to capture perf metrics from including https:// - e.g. https://google.com",
    )
    parser.addoption(
        "--csv",
        action="store",
        default="results.csv",
        help="The name of the output file to save the perf metrics to (including .csv).",
    )


@pytest.fixture(scope="function")
def start(py: Pylenium, request) -> str:
    """Specify which URL to capture web performance metrics from via the CLI."""

    def _start(url="https://google.com"):
        URL = request.config.getoption("--url") or url
        py.visit(URL)
        return URL

    return _start
