BUILDDIR=build
TOOLSDIR=tools
SOURCEDIR=en
SOURCES = $(SOURCEDIR)/*.md
TARGETS=$(addprefix $(BUILDDIR)/,$(wildcard $(SOURCES)))
TARGETNAME=OWASP Application Security Verification Standard 4.0

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

.PHONY: md $(BUILDDIR) pdf docx clean

all: $(TARGETS)	pdf docx

$(BUILDDIR): 
	@mkdir -p $(BUILDDIR)/en # make sure build dir exists

$(BUILDDIR)/en/%.md: $(BUILDDIR)
	sed -E 's#(\| ?)([0-9]{1,4})( ?\|)#\1[\2](https://cwe.mitre.org/data/definitions/\2.html)\3#; s#^(\| :?---:? \| :?)---( .*)#\| :-----: \| :---------------------------------------------------\2#; s#.(./images/)#\1#' $(subst build,.,$@) > $@
	 
md: $(BUILDDIR)
	pandoc $(PANDOC_MD_FLAGS) -o $(BUILDDIR)/source.md $(BUILDDIR)/$(SOURCES) 
	sed -Ei 's#../images/#./images/#' $(BUILDDIR)/source.md

pdf: 
	pandoc $(PANDOC_PDF_FLAGS) -o "$(BUILDDIR)/$(TARGETNAME).pdf" $(BUILDDIR)/en/*.md

tex:
	pandoc $(PANDOC_TEX_FLAGS) -o "$(BUILDDIR)/output.tex" $(BUILDDIR)/en/*.md
docx: 
	pandoc $(PANDOC_DOCX_FLAGS) -o "$(BUILDDIR)/$(TARGETNAME).docx" $(BUILDDIR)/en/*.md

clean:
	rm -rf $(BUILDDIR)/en
	rm $(BUILDDIR)/*.md
