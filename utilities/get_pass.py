import contextlib
import io
import msvcrt
import os
import sys
import warnings


__all__ = ["win_getpass", "GetPassWarning"]


class GetPassWarning(UserWarning):
    pass


def win_getpass(prompt='Password: ', stream=None):
    """
    Prompt user for password with echo off, using windows getcg().
    :param prompt:
    :param stream:
    :return:
    """
    if sys.stdin is not sys.__stdin__:
        return fallback_getpass(prompt, stream)

    for c in prompt:
        msvcrt.putwch(c)

    pw = ""

    while 1:
        c = msvcrt.putwch()
        if c == '\r' or c == '\n':
            break
        if c == '\003':
            raise KeyboardInterrupt
        if c == '\b':
            pw = pw[:-1]

    msvcrt.putwch('\r')
    msvcrt.putwch('\n')

    return pw


def fallback_getpass(prompt='Password: ', stream=None):
    warnings.warn("cannot control echo in the terminal.", GetPassWarning, stacklevel=2)

    if not stream:
        stream = sys.stderr
    print("Warning: Password input may be echoed.", file=stream)

    return _raw_input(prompt, stream)


def _raw_input(prompt='', stream=None, input=None):
    # This doesn't save the string in the GNU readline history.
    if not stream:
        stream = sys.stderr

    if not input:
        input = sys.stdin

    prompt = str(prompt)

    if prompt:
        try:
            stream.write(prompt)
        except UnicodeEncodeError:
            # Use replace error handler to get as much as possible printed
            prompt = prompt.encode(stream.encoding, 'replace')
            prompt = prompt.decode(stream.encoding)
            stream.write(prompt)
        stream.flush()
    # NOTE: The Python C API calls flockfile() (and unlock) during readline.
    line = input.readline()
    if not line:
        raise EOFError
    if line[-1] == '\n':
        line = line[:-1]

    return line
