#!/usr/bin/env python
import os
import time
import random
import os.path
import importlib
import pisano_example1

N = 400 if ('N' not in os.environ) else int(os.environ['N'])
M = 6000

examples = ["pisano_example1"] if ('IGNORE_EXAMPLE2' in os.environ) else ["pisano_example1", "pisano_example2"]

def get_samples():
    """ Make a list of N samples chosen from [2, M]
    """
    random.seed(11235)
    samples = random.sample(range(2, M+1), N)
    return sorted(samples)


def do_test(solution, samples, reference):
    """ Execute a function and compare the results with the reference
    """
    t0 = time.perf_counter()
    module = importlib.import_module(solution)
    func = module.get_pisano_numbers
    results = list(func(samples.copy()))
    t1 = time.perf_counter()
    runtime = (t1-t0) * 1000
    file_size = os.path.getsize(module.__file__)
    result = "PASS" if results == reference else "FAIL"
    return result, int(runtime), file_size


if __name__ == '__main__':
    samples = get_samples()
    reference = pisano_example1.get_pisano_numbers(samples)

    print(f"{'NAME':30s}{'RESULT':>8s}{'TIME':>8s}{'SIZE':>8s}{'SCORE':>8s}")
    for solution in [
            *examples,
            "pisano",
            "pisano_perf",
    ]:
        result, runtime, file_size = do_test(solution, samples, reference)
        score = runtime + file_size
        print(f"{solution:30s}{result:>8s}{runtime:8d}{file_size:8d}{score:8d}")
