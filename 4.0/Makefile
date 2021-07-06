BUILDDIR=build
TOOLSDIR=tools
SOURCEDIR=en
TEMPLATEDIR=templates
SOURCES = $(SOURCEDIR)/*.md
TARGETS=$(addprefix $(BUILDDIR)/,$(wildcard $(SOURCES)))
TARGETNAME=OWASP Application Security Verification Standard 4.0
EXPORT_JSON_TOOL=$(TOOLSDIR)/generate-json.py
EXPORT_CSV_TOOL=$(TOOLSDIR)/generate-csv.py
# Change LaTeX engine
PANDOC_MD_FLAGS=-f gfm -s -t markdown

PANDOC_PDF_FLAGS=-f markdown -s -t latex --pdf-engine=xelatex 

PANDOC_TEX_FLAGS=-f markdown -s -t latex 

PANDOC_DOCX_FLAGS= -s \
				  -t docx \
				  -f markdown \
				  --toc \
				  --columns 10000 \
				  --reference-doc=./templates/reference.docx 

PANDOC_ODT_FLAGS= -s \
				  -t odt \
				  -f markdown \
				  --toc \
				  --columns 10000 \
				  --reference-doc=./templates/reference.odt

.PHONY: md $(BUILDDIR) pdf docx odt clean

all: $(TARGETS)	pdf docx json csv

$(BUILDDIR): 
	@mkdir -p $(BUILDDIR)/en # make sure build dir exists

$(BUILDDIR)/en/%.md: $(BUILDDIR)
	sed -E 's#(\| ?)([0-9]{1,4})( ?\|)#\1[\2](https://cwe.mitre.org/data/definitions/\2.html)\3#; s#^(\| :?---:? \| :?)---( .*)#\| :-----: \| :---------------------------------------------------\2#; s#.(./images/)#\1#' $(subst build,.,$@) > $@
	 
md: $(BUILDDIR)
	pandoc $(PANDOC_MD_FLAGS) -o $(BUILDDIR)/source.md $(BUILDDIR)/$(SOURCES) 
	sed -Ei 's#../images/#./images/#' $(BUILDDIR)/source.md

pdf: 
	pandoc $(PANDOC_PDF_FLAGS) --include-in-header=$(TEMPLATEDIR)/header.tex  -o "$(BUILDDIR)/$(TARGETNAME).pdf" $(BUILDDIR)/en/*.md $(SOURCEDIR)/0x00-Header.yaml
	pandoc $(PANDOC_PDF_FLAGS) --include-in-header=$(TEMPLATEDIR)/header-eisvogel.tex -o "$(BUILDDIR)/$(TARGETNAME)2.pdf"  --template $(TEMPLATEDIR)/eisvogel.tex $(BUILDDIR)/en/*.md $(SOURCEDIR)/0x01-Header.yaml

tex:
	pandoc $(PANDOC_TEX_FLAGS) --include-in-header=$(TEMPLATEDIR)/header.tex -o "$(BUILDDIR)/output.tex" $(BUILDDIR)/en/*.md $(SOURCEDIR)/0x00-Header.yaml
	pandoc $(PANDOC_TEX_FLAGS) --include-in-header=$(TEMPLATEDIR)/header-eisvogel.tex -o "$(BUILDDIR)/output2.tex" --template $(TEMPLATEDIR)/eisvogel.tex $(BUILDDIR)/en/*.md $(SOURCEDIR)/0x01-Header.yaml

docx: 
	pandoc $(PANDOC_DOCX_FLAGS) -o "$(BUILDDIR)/$(TARGETNAME).docx" $(BUILDDIR)/en/*.md $(SOURCEDIR)/0x01-Header.yaml

odt: 
	pandoc $(PANDOC_ODT_FLAGS) -o "$(BUILDDIR)/$(TARGETNAME).odt" $(BUILDDIR)/en/*.md --metadata-file=$(SOURCEDIR)/0x01-Header.yaml

json:
	python3 $(EXPORT_JSON_TOOL) --file "$(BUILDDIR)/$(TARGETNAME).json"

csv:
	python3 $(EXPORT_CSV_TOOL) > "$(BUILDDIR)/$(TARGETNAME).csv"



clean:
	rm -rf $(BUILDDIR)/en
	rm $(BUILDDIR)/*.md
