The Pisano period implementation
================================

This is an attempt at [Vortech's Pisano Period challenge](https://github.com/vortechbv/pi-day-2023)

Current performance on i7-6700K CPU @ 4.20GHz:

    NAME                            RESULT    TIME    SIZE   SCORE
    pisano_example1                   PASS       0   33004   33004
    pisano_example2                   PASS  385491     794  386285
    pisano                            PASS      58     197     255

Notes:
------

- The implementation uses the that input range is `2..6000`. `p(1)` will run into an infinite loop.
