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
    pandoc -s -f gfm --reference-doc=../templates/reference.docx --columns 10000 --toc -t docx -o "../docs_$1/OWASP Application Security Verification Standard $2-$1.docx" *.md
	echo " done."
	echo -e ""
	echo -e "DOCX GENERATION MANUAL STEPS"
	echo -e "----------------------------"
	echo -e "After the docx file has been generated, do the following:"
	echo -e " - Select 'No' in the first prompt that appears"
	echo -e " - Move the 'Table of Contents' section to be just before the 'Frontispiece' section."
	echo -e " - Select the document heading (one of the first lines in the documrnt) which should say: 'OWASP Application"
	echo -e "   Security Verification Standard $2', go to 'Paragraph' > 'Line and Page Breaks' and"
	echo -e "   deselect 'Page break before'"
	echo -e " - Go to 'File' > 'Info' and set the 'Title' field to be 'OWASP Application Security Verification Standard $2'"
	echo -e " - Run the following VBA macro to fix Table settings:"
	echo -e "     "
	echo -e "     Dim tbl As Table"
	echo -e "     For Each tbl In ActiveDocument.Tables"
	echo -e "       tbl.Rows(1).HeadingFormat = True"
	echo -e "       tbl.Rows.AllowBreakAcrossPages = False"
	echo -e "     Next tbl"
	echo -e "     "
	echo -e " - Manually review the document and move any orphaned table headings or section headings to the"
	echo -e "   following page"
	echo -e " - Run 'Update table...' on the Table of Contents"
}

# generate_html() {
#     pandoc -s -f markdown_github -t html5 -o "../OWASP Application Security Verification Standard 4.0-$1.html" *.md
# }

lang="en"
vers="4.0"

if [ -z "$1" ]
then
	  lang="en"
else
      lang=$1
fi

if [ -z "$2" ]
then
      vers="4.0"
else
      vers=$2
fi

echo -n "Generating OWASP ASVS $vers ($lang)..."
if [ -d "$lang" ]; 
then
	cd "$lang"
	generate_docx $lang $vers
	# generate_html $lang
	cd ..
	
else
	echo " No OWASP ASVS found in directory $lang"
fi


echo 
echo "Generated OWASP Application Security Verification Standard $vers"
