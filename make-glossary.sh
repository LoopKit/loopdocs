#! /bin/bash
# File: make-glossary.sh
# execute this script after making changes to includes/tooltip-list.txt
# This will make a parallel change to docs/faqs/glossary.md
#
cat glossary_header.txt > docs/faqs/glossary.md
sed -E 's/\*\[([^]]+)\]: (.*)/\n\*\*<span translate="no">\1<\/span>\*\*\&nbsp\; (\1): \2/' includes/tooltip-list.txt >> docs/faqs/glossary.md
