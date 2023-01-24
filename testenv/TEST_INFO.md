# Automated testing
This file provides an overview of the test structures and invariants for the MCS 2022 project.
Tests are divided into two groups.

## Behaviour tests
Here are the structures that are describing simple situations.
The purpose of these tests is to verify the proper behavior of the system.

**Scoring:**
- If the theory has only one model and it is correct model = 1
- If the theory has more than one model and among them correct one = 0.5
- Otherwise = 0

Note that modelexpand will find at most two models, if one of them is correct you get 0.5.

**Tests:**
1. Stady behaviour: 
    - Description: No elevator requests, elevator should not do anything. 
    - Name: Scenario 1
    - Structure: S_t_1
2. Imidiat requet:
    - Description: One request at the start time point.
    - Name: Scenario 2
    - Structure: S_t_2
3. Request on the way
    - Description: Request apears on the elevators way (while moving to other request) 
    - Name: Scenario 3
    - Structure: S_t_3
4. Request belove
    - Description: Request apears belove the elevator while it goes up
    - Name: Scenario 4
    - Structure: S_t_4
5. Correct behaviour check
    - Description: More complex example with multiple requests
    - Name: Scenario 5
    - Structure: S_t_5
6. Correct behaviour check and efficiency 
    - Description: More complex example with multiple requests
    - Name: Scenario 6
    - Structure: S_t_6
7. Correct behaviour check and efficiency
    - Description: More complex example with multiple requests
    - Name: Scenario 6
    - Structure: S_t_6
8. Checking efficiency
    - Description: 50 time points example
    - Name: Scenario 6
    - Structure: S_t_6

**Meaning of results**
Meaning of the results table columns:
| Name | There is the same number of models | Number of models of student theory | There is a correct model | Final number of points |  

## Invariants tests
These tests are checking if the system entails certain invariants (in a structure):

**Scoring:**
- If the invariant is entailed = 1
- Otherwise = 0

**Invariants:**
1. Closed doors
    - Description: If the elevator moves the doors are closed!
    - Name: Invariant 1
    - Invariant: inv_1
2. Open doors
    - Description: Doors are only open when the elevator is answering requests!
    - Name: Invariant 2
    - Invariant: inv_2
3. Answering request
    - Description: If doors are open there is no unanswered request on that floor at the next time point. This invariant requires invariant two as an assumption.
    - Name: Invariant 3
    - Invariant: inv_3
4. Doors always closes
    - Description: Doors are never open for two consecutive time points. This invariant requires invariant two as an assumption.
    - Name: Invariant 4
    - Invariant: inv_4
5. New request
    - Description: Make request results in a new UnansweredRequest (if it is not already unanswered)
    - Name: Invariant 5
    - Invariant: inv_5

**Meaning of results**
Meaning of the results table columns:
| Name | Is invariant entailed | - | - | Final number of points |  

## How to run tests

**Command line**
1. Copy your `elevator.idp` into the testing environment (`testenv`) directory.
2. Note that the name must be `elevator.idp`
3. Run the IDP command form your command line: `idp -e automated_testing() automated_testing.idp`

**Web interface**
This approach should be done using online web IDP IDE.
Use this approach only in case you don't have IDP locally, or no command interface!
*Note* - This approach can fail due to the time limits of online IDP.

1. Coppy content of your `elevator.idp` at the begining of `automated_testing.idp`
    1. Copy all except `main()` procedure and include directives.
    2. Remove `include "elevator.idp"` from `automated_testing.idp`.
    3. Rename procedure `automated_testing()` to `main()` in `automated_testing.idp`.
2. Copy the file obtained in this way to [online IDP IDE](https://verne.cs.kuleuven.be/idp/server.html) or your local WEB-IDE
3. Run the specification.
