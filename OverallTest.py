from TestLoader import TestLoader
from TestLoaderTest import TestLoaderTest
from TestRunner import TestRunner
from TestResult import TestResult

result = TestResult()
loader = TestLoader()
suite = loader.make_suite(TestLoaderTest)

runner = TestRunner()
runner.run(suite)
