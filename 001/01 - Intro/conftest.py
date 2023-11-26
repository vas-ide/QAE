import datetime
import random

import pytest


@pytest.fixture()
def time(request):
    time_now = datetime.datetime.now()
    lst_time = []
    lst_time.append(time_now)
    print(f"Time - {lst_time[0]}")


    def fin():

        lst_time.append(time_now)
        print(f"Time - {lst_time[1]}")
        print(f"Total time - {lst_time[1] - lst_time[0]}")

    request.addfinalizer(fin)

@pytest.fixture()
def function_fixture(request):
    print(f"\n Hello from {request.scope} fixture!")
    yield
    print(f"\n Finalize from {request.scope} fixture!")


@pytest.fixture(scope="class")
def class_fixture(request):
    print(f"\n Hello from {request.scope} fixture!")
    def fin():
        print(f"\n Finalize from {request.scope} fixture!")
    request.addfinalizer(fin)

@pytest.fixture(scope="module")
def module_fixture(request):
    print(f"\n Hello from {request.scope} fixture!")
    def fin():
        print(f"\n Finalize from {request.scope} fixture!")
    request.addfinalizer(fin)

@pytest.fixture(scope="session")
def session_fixture(request):
    print(f"\n Hello from {request.scope.upper()} fixture!")
    def fin():
        print(f"\n Finalize from {request.scope.upper()} fixture!")
    request.addfinalizer(fin)



@pytest.fixture(params=[11, 12, 13, 14, 15, 16, 17, 18, 19])
def add_params(request):
    return request.param


@pytest.fixture
def rnd_number():
    return random.randint(1, 11)