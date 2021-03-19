# PMD Analyzer Action

[GitHub Action](https://github.com/features/actions) to run [PMD Analyzer](https://github.com/pmd/pmd) static code analysis checks.

## Action Result

By default, this action will succeed. Violations are annotated as warnings. See [Usage](#Usage) below.

## Usage

### Basic

Basic configuration to run PMD analyzer action.

```yaml
name: CI
on: [push]
jobs:
  analyze:
    name: Run PMD
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - id: pmd
        uses: rtjl/pmd-analyzer-action@v0.1.5-alpha
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
| should-throw-error | false |  Default is false. Set to true if you want: <br/>1) PMD warnings to appear as error messages instead of warnings on GitHub<br/>2) The action to fail instead of pass.

## Outputs

| Name | Description |
|------|-------------|
| no-of-violations    | No of violations found.

## Gotchas

Due to this [limitation](https://github.community/t/annotation-limitation/17998), only the first 10 violations will be displayed. Check logs to view all.
