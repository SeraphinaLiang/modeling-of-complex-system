# README

Here you can find simple instructions on how to run the tests:

## Running tests from the command line (Linux, Mac because IDP command line interface is required)

1. Copy your `elevator.idp` in this directory `testenv`.
2. Run the command `python run_all_tests.py`

## Running tests from the WEB-IDE

This test is adjusted to be performed using the Web IDE for IDP.

1. Copy `automated_testing_for_the_web.idp` file and `tests` directory to your project directory.
2. Add `include "automated_testing_for_the_web.idp"` at the end of your `elevator.idp` solution.
3. Edit your main procedure to contain only `automated_testing("Scenario 1")` and run it.
4. Run each test by replacing the argument of the `automated_testing` procedure. 
5. Possible arguments: `"Scenario x"` where x is 1..8 and `"Invariant x"` where x is 1..5

