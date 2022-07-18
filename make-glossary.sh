#! /bin/bash
# File: make-glossary.sh
# execute this script after making changes to includes/tooltip-list.txt
# This will make a parallel change to docs/faqs/glossary.md
#
cp -p includes/tooltip-list.txt tmp.txt
sed -i.bak 's/\*\[/\n\*\*/' tmp.txt
sed -i.bak 's/\]/\*\*/' tmp.txt
cat glossary_header.txt tmp.txt > docs/faqs/glossary.md
rm tmp.txt tmp.txt.bak
