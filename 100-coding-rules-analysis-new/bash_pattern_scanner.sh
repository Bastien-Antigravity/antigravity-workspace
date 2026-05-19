#!/bin/bash
echo "=== REPOSITORY ARCHITECTURE ===" > essence.txt
# Dump directory structure (ignores git and node_modules)
find . -not -path '*/\.*' -not -name 'node_modules' | sort | awk -F/ '{print strrep("  ", NF-2) $NF}' >> essence.txt

echo -e "\n=== ERROR HANDLING (GO) ===" >> essence.txt
# See how often 'if err != nil' is used vs panic
grep -r "if err != nil" . | wc -l | awk '{print "Standard error checks: "$1}' >> essence.txt
grep -r "panic(" . | wc -l | awk '{print "Panics: "$1}' >> essence.txt

echo -e "\n=== STRUCT/CLASS NAMING ===" >> essence.txt
# Extract class/struct names to see casing rules
grep -rho "type [A-Z][a-zA-Z0-9]* struct" . | sort | uniq -c | sort -nr | head -n 10 >> essence.txt
grep -rho "class [A-Z][a-zA-Z0-9]*" . | sort | uniq -c | sort -nr | head -n 10 >> essence.txt
