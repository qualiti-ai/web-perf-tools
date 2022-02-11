from pylenium.driver import Pylenium
import pytest
import csv


HEADERS = [
    "NAME",
    "QUALITI SCRIPTS DURATION",
    "TOTAL SCRIPTS DURATION",
    "FIRST CONTENTFUL PAINT",
    "PAGE LOAD TIME",
]
ROWS = []


@pytest.fixture(scope="session")
def save_results(project_root, request):
    """Save the results to a CSV file after the Test Run."""
    yield
    filename = request.config.getoption("--csv") or "results.csv"
    results_file = f"{project_root}/{filename}"
    with open(results_file, "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(HEADERS)
        csvwriter.writerows(ROWS)


def test_web_performance_metrics(py: Pylenium, start, request, save_results):
    # 1. Visit URL and capture performance metrics
    start("https://www.drivingsales.com/hcm")
    metrics = py.performance.get()
    qualiti_resources = [x for x in metrics.resources if "qualiti.ai" in x.name]

    # 2. Extract and transform metrics as needed
    name = request.node.name
    qualiti_scripts_duration = sum([x.duration for x in qualiti_resources])
    total_scripts_duration = sum([x.duration for x in metrics.resources])
    first_contentful_paint = metrics.time_to_first_contentful_paint()
    page_load_time = metrics.page_load_time()

    # 3. Add metrics to results list
    ROWS.append(
        [
            name,
            qualiti_scripts_duration,
            total_scripts_duration,
            first_contentful_paint,
            page_load_time,
        ]
    )


def test_foo(py: Pylenium, start):
    # 1. Visit URL and capture performance metrics
    start("https://www.drivingsales.com/hcm")
    metrics = py.performance.get()
    assert metrics
