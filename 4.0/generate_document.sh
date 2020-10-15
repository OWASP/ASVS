#!/bin/bash

echo "OWASP Markdown Conversion Tool"
echo ""

function command_exists () {
    command -v $1 >/dev/null 2>&1;
}

if ! command_exists pandoc; then
    echo "Error: Please install pandoc. Cannot continue"
    exit;
fi

generate_docx() {
    pandoc -s -f gfm --reference-doc=../templates/reference.docx --columns 10000 --toc -t docx -o "../OWASP Application Security Verification Standard 4.0-$1.docx" *.md
	# After this process, move the Table of Contents and change the style 
	# of the first Heading 1 so it is on the first page
}

# generate_html() {
#     pandoc -s -f markdown_github -t html5 -o "../OWASP Application Security Verification Standard 4.0-$1.html" *.md
# }

generate() {
    echo -n "Generating OWASP ASVS 4.0 ($1)..."
    if [ -d "$1" ]; 
    then
        cd "$1"
        generate_docx $1
        # generate_html $1
        cd ..
        echo " done."
    else
        echo " No OWASP ASVS found in directory $1"
    fi
}

# Arabic
#generate "ar"

# Brazil
#generate "br"

# Chinese 
#generate "cn"

# Czech
#generate "cz"

# English
generate "en"

# French 
#generate "fr"

# German
# generate "de"

# Hebrew
#generate "heb"

# Italian
#generate "it"

# Japanese
#generate "jp"

# Korean
#generate "kr"

# Spanish
# generate "es"

# Ukraine
#generate "ukr"

echo 
echo "Generated OWASP Application Security Verification Standard 4.0"
