import sys
import os
from behave.fixture import use_fixture_by_tag, fixture_call_params
print(os.path.abspath("."))
sys.path.append('/Users/zhouguosheng/PythonBehave/BehaveTest')
from BehaveTest.features.fixtures import *
from BehaveTest.utils.utils import *

fixture_registry1 = {
    # "fixture.test.fixture": test_fixture
}


def before_scenario(context, scenario):
    log('before %s -- %s' % (context.feature, context.scenario))
    use_fixture_by_tag(tag='fixture.test.fixture', context=context, fixture_registry=fixture_registry1)

def after_scenario(context, scenario):
    log('after %s -- %s' % (context.feature, context.scenario))
    use_fixture_by_tag(tag='fixture.test.fixture', context=context, fixture_registry=fixture_registry1)


# def log(message):
#     with open('./log.txt', 'a') as f:
#         f.write(message)
#         f.write(os.linesep)
#         f.flush()

if __name__ == '__main__':
    print('test')