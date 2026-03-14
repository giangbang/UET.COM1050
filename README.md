# UET.COM1050
This repository contains weekly programming problems.

## How to Work on an Assignment
1. Fork this repository.
2. Clone your fork:
    ```bash
    git clone <your-fork-url>
    cd <repo-name>
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    you are recommended to use virtual environments, if possible.
4. All assignments are located in their respective `week{i}` folders (create if needed, see `week1` and `week2` for examples).
Write your solution in Python files named `week{i}/p{j}.py`.
Each file must contain a Python function named `solution` that takes *no input arguments*. This function corresponds to problem `j` in week `i`.
The test files expect this function structure.
5. Repeat the steps 4 for other assignments.

Steps 1–3 only need to be completed once.
## Running Tests Locally

Run all tests:
```bash
pytest
```
Run tests for a specific problem:
```bash
pytest tests/week1/test_p1.py
```
Run all tests for a specific week:
```bash
pytest tests/week1
```
All test cases are located in the `tests` folder. Please refrain from reading them.
## Submitting Your Work
Commit your changes:
```bash
git add .
git commit -m "Solve week1 p1"
```
Push to remote:
```bash
git push origin master
```

## Note on submissions
- All submissions *should normally be made through the university’s main website*.
Submissions on github are intended only as a backup option in unexpected circumstances.
- Please submit on time. **Commit timestamps may be used to verify deadlines.** Each week should be submitted on a **separate branch** so that the commit history and timestamps for that week are preserved.