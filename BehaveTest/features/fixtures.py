from behave import fixture
import os

def log(message):
    with open('./log.txt', 'a') as f:
        f.write(message)
        f.write(os.linesep)
        f.flush()

@fixture
def test_fixture(context, *args, **kwargs):
    # -- SETUP-FIXTURE PART:
    log('in test_fixture setup')
    # -- CLEANUP-FIXTURE PART:
    log('in test_fixture cleanup')

if __name__ == '__main__':
    pass