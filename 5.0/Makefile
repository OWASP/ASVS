DISTDIR=dist
TOOLSDIR=tools
SOURCEDIR=en
TEMPLATEDIR=templates
SOURCES = $(SOURCEDIR)/*.md
TARGETS=$(addprefix $(DISTDIR)/,$(wildcard $(SOURCES)))
TARGETNAME=OWASP_Application_Security_Verification_Standard-5_x
EXPORT_TOOL=$(TOOLSDIR)/export.py

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

.PHONY: md $(DISTDIR) pdf docx odt clean tex

all: $(TARGETS)	pdf docx json json_flat csv xml

$(DISTDIR): 
	@mkdir -p $(DISTDIR)/en # make sure distribution dir exists

$(DISTDIR)/en/%.md: $(DISTDIR)
	sed -E 's#(\| ?)([0-9]{1,4})( ?\|)#\1[\2](https://cwe.mitre.org/data/definitions/\2.html)\3#; s#^(\| :?---:? \| :?)---( .*)#\| :-----: \| :---------------------------------------------------\2#; s#.(./images/)#\1#; s#(\\)([rntv])#\\escape{\2}#g' $(subst dist,.,$@) > $@

md: $(DISTDIR)
	pandoc $(PANDOC_MD_FLAGS) -o $(DISTDIR)/source.md $(DISTDIR)/$(SOURCES) 
	sed -Ei 's#../images/#./images/#' $(DISTDIR)/source.md

pdf: $(TARGETS) 
	pandoc $(PANDOC_PDF_FLAGS) --include-in-header=$(TEMPLATEDIR)/header-eisvogel.tex -o "$(DISTDIR)/$(TARGETNAME).pdf"  --template $(TEMPLATEDIR)/eisvogel.tex $(DISTDIR)/en/*.md $(SOURCEDIR)/0x01-Header.yaml

tex: $(TARGETS)
	pandoc $(PANDOC_TEX_FLAGS) --include-in-header=$(TEMPLATEDIR)/header-eisvogel.tex -o "$(DISTDIR)/output.tex" --template $(TEMPLATEDIR)/eisvogel.tex $(DISTDIR)/en/*.md $(SOURCEDIR)/0x01-Header.yaml

docx: $(TARGETS)
	pandoc $(PANDOC_DOCX_FLAGS) -o "$(DISTDIR)/$(TARGETNAME).docx" $(DISTDIR)/en/*.md $(SOURCEDIR)/0x01-Header.yaml

odt: $(TARGETS)
	pandoc $(PANDOC_ODT_FLAGS) -o "$(DISTDIR)/$(TARGETNAME).odt" $(DISTDIR)/en/*.md --metadata-file=$(SOURCEDIR)/0x01-Header.yaml

json:
	python3 $(EXPORT_TOOL) --format json --language "$(SOURCEDIR)" > "$(DISTDIR)/$(TARGETNAME).json"

json_flat:
	python3 $(EXPORT_TOOL) --format json_flat --language "$(SOURCEDIR)" > "$(DISTDIR)/$(TARGETNAME).flat.json"

csv:
	python3 $(EXPORT_TOOL) --format csv --language "$(SOURCEDIR)" > "$(DISTDIR)/$(TARGETNAME).csv"

xml:
	python3 $(EXPORT_TOOL) --format xml --language "$(SOURCEDIR)" > "$(DISTDIR)/$(TARGETNAME).xml"

.PHONY: prod
prod:
	cp -R dist/* .

clean:
	rm -rf $(DISTDIR)/en
	rm -f $(DISTDIR)/*.md
