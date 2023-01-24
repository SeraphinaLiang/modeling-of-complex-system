import sys, os
from subprocess import PIPE, run


#Run the test

def run_the_test(test):
    cmd_result = run(["idp", "-e", "automated_testing('"+test+"')", "automated_testing.idp"], stdout=PIPE, stderr=PIPE, universal_newlines=True)

    if (cmd_result.returncode != 0):
        if ("Error: Inference timed-out" in cmd_result.stderr):
            print(test+", - , - , time-out , 0")
        else:
            print("Return code: " + str(cmd_result.returncode) + "\n")
            print(cmd_result.stderr)
    else:
        #print(cmd_result.stdout)
        for line in (cmd_result.stdout.splitlines()): 
            if line.startswith(test):
                print(line)



run_the_test("Scenario 1")
run_the_test("Scenario 2")
run_the_test("Scenario 3")
run_the_test("Scenario 4")
run_the_test("Scenario 5")
run_the_test("Scenario 6")
run_the_test("Scenario 7")
run_the_test("Scenario 8")
run_the_test("Invariant 1")
run_the_test("Invariant 2")
run_the_test("Invariant 3")
run_the_test("Invariant 4")
run_the_test("Invariant 5")