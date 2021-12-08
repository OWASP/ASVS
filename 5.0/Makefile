BUILDDIR=build
DISTDIR=dist
TOOLSDIR=tools
SOURCEDIR=en
TEMPLATEDIR=templates
SOURCES = $(SOURCEDIR)/*.md
TARGETS=$(addprefix $(BUILDDIR)/,$(wildcard $(SOURCES)))
TARGETNAME=OWASP Application Security Verification Standard 5.x
#EXPORT_JSON_TOOL=$(TOOLSDIR)/generate-json.py
EXPORT_TOOL=$(TOOLSDIR)/export.py
#EXPORT_CSV_TOOL=$(TOOLSDIR)/generate-csv.py

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

.PHONY: md $(BUILDDIR) $(DISTDIR) pdf docx json json_flat csv xml odt clean

all: $(TARGETS)	pdf docx json json_flat csv xml

$(BUILDDIR): 
	@mkdir -p $(BUILDDIR)/en # make sure build dir exists

$(DISTDIR): 
	@mkdir -p $(DISTDIR)/en # make sure distribution dir exists

$(BUILDDIR)/en/%.md: $(BUILDDIR)
	sed -E 's#(\| ?)([0-9]{1,4})( ?\|)#\1[\2](https://cwe.mitre.org/data/definitions/\2.html)\3#; s#^(\| :?---:? \| :?)---( .*)#\| :-----: \| :---------------------------------------------------\2#; s#.(./images/)#\1#' $(subst build,.,$@) > $@
	 
md: $(BUILDDIR)
	pandoc $(PANDOC_MD_FLAGS) -o $(BUILDDIR)/source.md $(BUILDDIR)/$(SOURCES) 
	sed -Ei 's#../images/#./images/#' $(BUILDDIR)/source.md

pdf: md $(DISTDIR)
	pandoc $(PANDOC_PDF_FLAGS) --include-in-header=$(TEMPLATEDIR)/header-eisvogel.tex -o "$(DISTDIR)/$(TARGETNAME).pdf"  --template $(TEMPLATEDIR)/eisvogel.tex $(BUILDDIR)/en/*.md $(SOURCEDIR)/0x00-Header.yaml

tex: md $(DISTDIR)
	pandoc $(PANDOC_TEX_FLAGS) --include-in-header=$(TEMPLATEDIR)/header-eisvogel.tex -o "$(DISTDIR)/$(TARGETNAME).tex" --template $(TEMPLATEDIR)/eisvogel.tex $(BUILDDIR)/en/*.md $(SOURCEDIR)/0x00-Header.yaml

docx: md $(DISTDIR)
	pandoc $(PANDOC_DOCX_FLAGS) -o "$(DISTDIR)/$(TARGETNAME).docx" $(BUILDDIR)/en/*.md $(SOURCEDIR)/0x01-Header.yaml

odt: md $(DISTDIR)
	pandoc $(PANDOC_ODT_FLAGS) -o "$(DISTDIR)/$(TARGETNAME).odt" $(BUILDDIR)/en/*.md --metadata-file=$(SOURCEDIR)/0x01-Header.yaml

json: $(DISTDIR)
	python3 $(EXPORT_TOOL) --format json --language "$(SOURCEDIR)" > "$(DISTDIR)/$(TARGETNAME).json"

json_flat:
	python3 $(EXPORT_TOOL) --format json_flat --language "$(SOURCEDIR)" > "$(DISTDIR)/$(TARGETNAME).flat.json"

csv:
	python3 $(EXPORT_TOOL) --format csv --language "$(SOURCEDIR)" > "$(DISTDIR)/$(TARGETNAME).csv"

xml:
	python3 $(EXPORT_TOOL) --format xml --language "$(SOURCEDIR)" > "$(DISTDIR)/$(TARGETNAME).xml"

clean:
	rm -rf $(BUILDDIR)/en
	rm $(BUILDDIR)/*.md
