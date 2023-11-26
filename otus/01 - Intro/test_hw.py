import math


class TestAdd:

    def test_string(self, time, function_fixture, class_fixture, module_fixture, session_fixture):
        surname = "V______n"
        name = "A_____y"
        example = f"V______n A_____y"
        print(f"Merge string: {surname} {name} ---> {example}")
        assert example == f"{surname} {name}"

    def test_degree(self, time, class_fixture, module_fixture, session_fixture, add_params):
        answer = math.pow(add_params, 10)
        print(f"{add_params} возведение в 10 степень {answer}")
        assert answer == add_params ** 10

    def test_random_degree(self, time, class_fixture, module_fixture, session_fixture, add_params, rnd_number):
        degree = rnd_number
        answer = math.pow(add_params, degree)
        print(f"{add_params} возведение в {degree} степень {answer}")
        assert answer == add_params ** degree
