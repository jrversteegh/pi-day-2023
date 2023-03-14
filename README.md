The Pisano period implementation
================================

This is an attempt at [Vortech's Pisano Period challenge](https://github.com/vortechbv/pi-day-2023)

Current performance on i7-6700K CPU @ 4.20GHz:

    NAME                            RESULT    TIME    SIZE   SCORE
    pisano_example1                   PASS       0   33004   33004
    pisano_example2                   PASS  399125     794  399919
    pisano                            PASS      57     160     217
    pisano_perf                       PASS      54     280     334


Notes:
------

- The implementation uses that input range is `2..6000`. `p(1)` will run into an infinite loop.
- There are optimizations possible by observing that the pisano periods have various mathematical
  properties, like for example that pisano periods for N>2 are even, but considering the small runtime,
  the additional code size will not be compensated for. This might be different for a much larger
  problem size however!
- The `pisano_perf` module improves performance using multiprocessing, but only for large(r) N, e.g. for N=5999:

    NAME                            RESULT    TIME    SIZE   SCORE
    pisano_example1                   PASS       0   33004   33004
    pisano                            PASS     901     160    1061
    pisano_perf                       PASS     285     282     567
