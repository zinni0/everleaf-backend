


# Contributing Guidelines

Thank you for your interest in contributing to this project!  
Before submitting a pull request (PR) or issue, please read these guidelines.

---

## 1. How to Contribute

1. **Fork the repository** and create your branch:
   ```bash
   git checkout -b feature/my-feature
   ```
2. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```
   or, if you use Poetry / pyproject.toml, run the appropriate install command.
3. Make your changes, following the code style and formatting rules:

    * Python code: [PEP 8](https://www.python.org/dev/peps/pep-0008/)
    * Formatter: `black`
    * Import sorting: `isort`
    * Linting: `pylint`
4. Run pre-commit hooks (if installed) to automatically check formatting and linting:
   ```bash
   pre-commit run --all-files
   ```
5. Write tests if applicable, using `pytest`. 
6. Run all tests locally before creating a PR:

   ```bash
   pytest
   ```

---

## 2. Creating a Pull Request

* Push your branch to your fork.
* Open a **Pull Request** against `develop`.
* Use the provided **PR template**.
* Assign appropriate **labels** if you have permission.
* **Note:** All PRs are reviewed and merged **only by the repository maintainer**.

---

## 3. Reporting Issues

* Use the **issue templates** (`bug_report`, `feature_request`, `blank`) to provide clear information.
* Include steps to reproduce bugs, expected behavior, and environment details.

---

## 4. Code of Conduct

Be respectful and considerate. Harassment or discrimination will not be tolerated.

---

## 5. Why Review Control Matters

Even though this is a public repository:

* Only the maintainer merges PRs.
* Reviews ensure quality, consistency, and maintainability of the code.
* Following templates and guidelines helps speed up the review process.

---

Thank you for helping improve the project!
