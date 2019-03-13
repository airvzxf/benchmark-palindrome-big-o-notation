#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Main script which start the benchmark.
"""


# noinspection PyCompatibility
def main() -> None:
    """
    Start the python benchmarks between iterate the full string and iterate the half of the string.

    :rtype: None
    """
    from multiprocessing import Process
    from palindrome.full import full
    from palindrome.half import half

    processing = []

    files = [
        '../generate_palindrome/cmake-build-release/00-tiny.txt',
        '../generate_palindrome/cmake-build-release/01-small.txt',
        '../generate_palindrome/cmake-build-release/02-medium.txt',
        '../generate_palindrome/cmake-build-release/03-big.txt',
        '../generate_palindrome/cmake-build-release/04-huge.txt',
        '../generate_palindrome/cmake-build-release/05-immense.txt',
    ]

    for file in files:
        with open(file) as phrase_file:
            phrase_full = phrase_file.read()
            phrase_full_size = len(phrase_full)

        with open(file) as phrase_file:
            phrase_half = phrase_file.read()
            phrase_half_size = len(phrase_half)

        processing.append(
            Process(
                target=full,
                args=(phrase_full,),
                name='Full_%i' % phrase_full_size
            )
        )
        processing[-1].start()

        processing.append(
            Process(
                target=half,
                args=(phrase_half,),
                name='Half_%i' % phrase_half_size
            )
        )
        processing[-1].start()

        for processor in processing:
            # processor.start()
            processor.join()

    return None


if __name__ == "__main__":
    main()
