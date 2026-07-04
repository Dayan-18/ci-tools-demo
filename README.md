# CI Tools Demo — Same Pipeline, Three Tools

Demo repo for the article **"CI/CD Testing Tools Compared: the Same Pipeline in GitHub Actions, GitLab CI and Jenkins"**.

One Python test suite (10 tests), one pipeline (install → test → publish JUnit report), written for three CI tools so you can compare their syntax side by side:

| File | Tool | Status |
|---|---|---|
| `.github/workflows/tests.yml` | GitHub Actions | ✅ runs live in this repo (Actions tab) |
| `.gitlab-ci.yml` | GitLab CI | reference (runs if repo is mirrored to GitLab) |
| `Jenkinsfile` | Jenkins | reference (runs on any Jenkins with Docker) |

## Run the tests locally

```bash
pip install -r requirements.txt
pytest test_calculator.py -v
```
