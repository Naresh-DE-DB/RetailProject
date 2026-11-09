import pytest
from lib.Utils import get_spark_session

@pytest.fixture
def spark():
    "Create spark session"
    spark_session = get_spark_session('LOCAL')
    yield spark_session
    spark_session.stop()

@pytest.fixture
def expected_result(spark):
    "expected result dataframe"
    results_schema = "state STRING, count INT"
    return spark.read.csv('data/test_result/state_aggregate.csv', schema=results_schema)
