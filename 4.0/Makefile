PROJDIR=$(realpath $(CURDIR))
LANGDIRS=ar en es fr zh-cn
# Add the language directories to the project directory
SOURCEDIRS=$(foreach dir, $(LANGDIRS), $(addprefix $(PROJDIR)/, $(dir)))
# Create build and dist directories and language subdirectories
BUILDDIR=$(PROJDIR)/build
BUILDDIRS=$(foreach dir, $(LANGDIRS), $(addprefix $(BUILDDIR)/, $(dir)))
DISTDIR=$(PROJDIR)/dist
DISTDIRS=$(foreach dir, $(LANGDIRS), $(addprefix $(DISTDIR)/, $(dir)))

TOOLSDIR=$(PROJDIR)/tools
TEMPLATEDIR=$(PROJDIR)/templates
SOURCES = $(SOURCEDIR)/*.md
TARGETS=$(addprefix $(BUILDDIR)/,$(wildcard $(SOURCES)))
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

.PHONY: md $(BUILDDIRS) $(DISTDIRS) pdf docx json json_flat csv xml odt tex clean

all: $(TARGETS)	pdf docx json json_flat csv xml

# make sure distribution dir exists
$(DISTDIR): 
	@mkdir -p $(DISTDIR)

# make sure build dir exists
$(BUILDDIR): 
	@mkdir -p $(BUILDDIR)/en 

# transform origin md files. needed by the next stages
$(BUILDDIR)/en/%.md: $(BUILDDIR)
	echo "from $(subst $(BUILDDIR),.,$@) to  $@"
	sed -E 's#(\| ?)([0-9]{1,4})( ?\|)#\1[\2](https://cwe.mitre.org/data/definitions/\2.html)\3#; s#^(\| :?---:? \| :?)---( .*)#\| :-----: \| :---------------------------------------------------\2#; s#.(./images/)#\1#; s#(\\)([rntv])#\\escape{\2}#g' $(subst $(BUILDDIR),.,$@) > $@
	 
md: $(BUILDDIR) $(DISTDIR)
	pandoc $(PANDOC_MD_FLAGS) -o $(DISTDIR)/source.md $(BUILDDIR)/$(SOURCES) 
	sed -Ei 's#../images/#./images/#' $(DISTDIR)/source.md

pdf: $(TARGETS) $(DISTDIR)
	pandoc $(PANDOC_PDF_FLAGS) --include-in-header=$(TEMPLATEDIR)/header-eisvogel.tex -o "$(DISTDIR)/$(TARGETNAME).pdf"  --template $(TEMPLATEDIR)/eisvogel.tex $(BUILDDIR)/en/*.md $(SOURCEDIR)/0x00-Header.yaml

tex: $(TARGETS) $(DISTDIR)
	pandoc $(PANDOC_TEX_FLAGS) --include-in-header=$(TEMPLATEDIR)/header-eisvogel.tex -o "$(DISTDIR)/$(TARGETNAME).tex" --template $(TEMPLATEDIR)/eisvogel.tex $(BUILDDIR)/en/*.md $(SOURCEDIR)/0x00-Header.yaml

docx: $(TARGETS) $(DISTDIR)
	pandoc $(PANDOC_DOCX_FLAGS) -o "$(DISTDIR)/$(TARGETNAME).docx" $(BUILDDIR)/en/*.md $(SOURCEDIR)/0x00-Header.yaml

odt: $(TARGETS) $(DISTDIR)
	pandoc $(PANDOC_ODT_FLAGS) -o "$(DISTDIR)/$(TARGETNAME).odt" $(BUILDDIR)/en/*.md --metadata-file=$(SOURCEDIR)/0x00-Header.yaml

json: $(DISTDIR)
	python3 $(EXPORT_TOOL) --format json --language "$(SOURCEDIR)" > "$(DISTDIR)/$(TARGETNAME).json"

json_flat: $(DISTDIR)
	python3 $(EXPORT_TOOL) --format json_flat --language "$(SOURCEDIR)" > "$(DISTDIR)/$(TARGETNAME).flat.json"

csv: $(DISTDIR)
	python3 $(EXPORT_TOOL) --format csv --language "$(SOURCEDIR)" > "$(DISTDIR)/$(TARGETNAME).csv"

xml: $(DISTDIR)
	python3 $(EXPORT_TOOL) --format xml --language "$(SOURCEDIR)" > "$(DISTDIR)/$(TARGETNAME).xml"


clean:
	rm -rf $(BUILDDIR)/en
	rm -rf $(DISTDIR)/en
	rm -f $(DISTDIR)/*.md
	rm -f $(DISTDIR)/*.tex
	rm -f $(DISTDIR)/*.docx
	rm -f $(DISTDIR)/*.pdf
	rm -f $(DISTDIR)/*.json
	rm -f $(DISTDIR)/*.csv
	rm -f $(DISTDIR)/*.xml
