#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test that the batch renamer handles filenames correctly.

Here's an excerpt from Python Crash Course on page 217. Certain portions
have been accentuated for emphasis.:

Unit Tests and Test Cases
--------------------------
The module :mod:`unittest` from the Python standard library provides tools
for testing your code. A **unit test** verifies that one specific aspect
of a function’s behavior is correct. A **test case** is a collection of
unit tests that together prove that a function behaves as it’s supposed
to, within the full range of situations you expect it to handle.

A good test case considers all the possible kinds of input a function could
receive and includes tests to represent each of these situations.
A test case with **full coverage** includes a full range of unit
tests covering all the possible ways you can use a function. Achieving full
coverage on a large project can be daunting. It’s often good enough to
write tests for your code’s critical behaviors and then aim for full
coverage only if the project starts to see widespread use.

A Passing Test
---------------
The syntax for setting up a test case takes some getting used to, but once
you’ve set up the test case it’s straightforward to add more unit tests
for your functions. To write a test case for a function, import the
:mod:`unittest` module and the function you want to test. Then create a
class that inherits from :class:`unittest.TestCase()`, and write a series
of methods to test different aspects of your function’s behavior.


The module itself
------------------
Now let's go on and go through this module line by line so you know what is
required for a unit testing module.

First, we import :mod:`unittest` and the function we want to test,
get_formatted_name(). We create a class called NamesTestCase, which will
contain a series of unit tests for get_formatted_name(). You can name the
class anything you want, but it’s best to call it something related to the
function you’re about to test and to use the word Test in the class name.
This class must inherit from the class :class:`unittest.TestCase()` so
Python knows how to run the tests you write.

NamesTestCase contains a single method that tests one aspect of
get_formatted_name(). We call this method test_first_last_name() because
we’re verifying that names with only a first and last name are formatted
correctly. Any method that starts with `test_` will be run automatically
when we run `test_name_function.py`. Within this test method, we call the
function we want to test and store a return value that we’re interested in
testing. In this example we call get_formatted_name() with the arguments
`janis` and `joplin`, and store the result in formatted_name.

We use one of unittest’s most useful features: an ``assert`` method.
Assert methods verify that a result you received matches the result you
expected to receive. In this case, because we know get_formatted_name() is
supposed to return a capitalized, properly spaced full name, we expect
the value in formatted_name to be Janis Joplin. To check if this is true,
we use :mod:`unittest`’s :func:`~unittest.TestCase.assertEqual()` method
and pass it formatted_name and `Janis Joplin`.

"""
import unittest

from pyutil import batch_renamer


class BatchTestCase(unittest.TestCase):
    """Tests for :mod:`~pyutil.batch_renamer.."""

    def test_fix_extension(self):
        """Do filenames like 'shutil.rst.txt' work?

        It was at this moment that I realized how not finished that script is.
        """
        # batch_renamer

    def test_fix_multipart_filename(self):
        """todo"""
        pass


if __name__ == "__main__":
    unittest.main()
