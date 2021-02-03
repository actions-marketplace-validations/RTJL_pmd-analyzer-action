# PMD Analyzer Action

[GitHub Action](https://github.com/features/actions) to run [PMD Analyzer](https://github.com/pmd/pmd) static code analysis checks.

## Success Criteria

By default, this action will succeed. See [Usage](#Usage) below.

## Usage

### Basic

Basic configuration that will run PMD.

```yaml
name: CI
on: [pull_request]
jobs:
  analyze:
    name: Run PMD
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - id: pmd
      uses: rtjl/pmd-analyzer-action@v0.1.3-alpha
      with:
        pmd-version: '6.31.0'
        source-path: './src'
        rule-path: './PMD.Rules.xml'
```

## Inputs

| Name | Default | Description |
|------|---------|-------------|
| pmd-version    | 6.31.0   | PMD version to use.
| source-path    | \<none>  | The path for PMD to analyze.
| rule-path      | \<none>  | The ruleset file for PMD to use.

## Outputs

| Name | Description |
|------|-------------|
| no-of-violations    | No of violations found.
