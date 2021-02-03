wget "https://github.com/pmd/pmd/releases/download/pmd_releases%2F$1/pmd-bin-$1.zip"
unzip "pmd-bin-$1.zip"
cmd="pmd-bin-$1/bin/run.sh pmd -d $2 -R $3  -failOnViolation false -f json > pmd-output.json"
eval "$cmd"