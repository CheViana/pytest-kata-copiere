# Pytest kata series: copiere

Kata exercise to practice pytest patching.

- Checkout unsolved version from `unsolved` branch. 
- Implement test cases for copiere function.
- Compare your solution to the solution in `solved` branch.


## To run tests:

Run python tests for copiere:

```sh
    > mkvirtualenv --python=python3.9 copiere
    > pip install -r requirements/test.txt --upgrade
    > pip install -e .
    > pytest
```

## To run copiere:

When run as main, script expects in working dir:
    - example.txt
    - sour/ex1.txt
    - sour/ex2.txt
    - dest/ - empty directory

Run:

```sh
    > mkvirtualenv --python=python3.9 copiere
    > pip install -r requirements/base.txt --upgrade
    > pip install -e .
    > python src/copiere/main.py
```