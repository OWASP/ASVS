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

if ! command_exists xelatex; then
    echo "Warning: Install xelatex to produce PDF output"
fi

echo ""

generate_pdf() {
    if command_exists xelatex; then
	    # pandoc -N --template ../templates/template.tex --variable mainfont="Merriweather" --variable sansfont="Roboto" --variable monofont="Menlo" --variable fontsize=10pt --variable version=1.17.2 --latex-engine=xelatex --toc -fmarkdown-implicit_figures -o "../OWASP-Top-10-2017-$1.pdf" *.md
        echo " no PDF generated due to bugs"
    else
        echo " could not generate PDF, missing pdflatex"
    fi
}

generate_docx() {
    pandoc -s -f gfm --reference-docx=../templates/reference.docx --columns 10000 -t docx -o "../OWASP Application Security Verification Standard $1.docx" *.md
}

generate_html() {
    pandoc -s -f gfm -t html5 --css custom.css -o "../OWASP Application Security Verification Standard $1.html" *.md
}

generate() {
    echo -n "Generating OWASP ASVS ($1)..."
    if [ -d "$1" ]; 
    then
        cd "$1"
        generate_docx $1
        generate_pdf $1
        generate_html $1
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
generate "de"

# Hebrew
#generate "heb"

# Italian
#generate "it"

# Japanese
#generate "jp"

# Korean
#generate "kr"

# Spanish
generate "es"

# Ukraine
#generate "ukr"

echo 
echo "Generated OWASP Application Security Verification Standard"
