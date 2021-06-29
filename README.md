# Accessibility Monitoring Platform integration tests

Integration tests for the Central Digital and Data Office's accessibility monitoring platform

## Set up

* This guide assumes that you are using a Mac, with `zsh` as your Terminal and VS Code.
* [Install Python, a virtual environment and Pylenium](https://docs.pylenium.io/getting-started/virtual-environments)
* Set up your IDE to use `pytest` as the default test runner. In VS Code on Mac, use Cmd + Shift + P, select Python: Configure Tests and choose `pytest`.

### Optional VS code setup

* To stop "Run tests | Debug tests" appearing in VS Code as you type, add `"editor.codeLens": false` to your `settings.json` file.

## Run tests

```python
python -m pytest tests
```

To run with "print" outputs displayed, use `python -m pytest -s tests`

## Environment variables

The platform requires a login. To avoid publishing usernames and passwords on GitHub, the login details can be set up as follows:

Set up a `.zshrc` file in your home directory with the following alias

```zsh
alias pyrun="AMP_USERNAME='email@example.com' AMP_PASSWORD='MySuperSecretPassword' python -m pytest -s tests"
```

You can then run tests by typing `pyrun`.