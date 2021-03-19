import json
import sys

shouldThrowError = sys.argv[1]

noOfViolations_output_template = "::set-output name=no-of-violations::{no_of_violations}"
output_template = "::warning file={file},line={line},col={col}::{msg}"
if shouldThrowError:
  output_template = "::error file={file},line={line},col={col}::{msg}"

warning_message_template = "Violation found in {fileName} from Line:{startLine}, Col:{startCol} to Line:{endLine}, Col:{endCol}. " \
      "{ruleset} - {rule}: {description} " \
      "({url})."

warning_message_list = []

with open('pmd-output.json') as file:
  data = json.load(file)
  for file in data['files']:
    for v in file['violations']:
      warning_message = warning_message_template.format(ruleset = v['ruleset'], rule = v['rule'], description = v['description'], 
              startLine = v['beginline'], endLine = v['endline'], startCol = v['begincolumn'], endCol = v['endcolumn'], 
              url = v['externalInfoUrl'], fileName = file['filename'])
      warning_output = output_template.format(file = file['filename'], line = v['beginline'], col = v['begincolumn'], msg = warning_message)
      warning_message_list.append(warning_output)

print(noOfViolations_output_template.format(no_of_violations = len(warning_message_list)))

for warning_message in warning_message_list:
  print(warning_message)
