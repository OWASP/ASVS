BUILDDIR=build
TOOLSDIR=tools
SOURCEDIR=en
SOURCES = $(SOURCEDIR)/*.md
TARGETS=$(addprefix $(BUILDDIR)/,$(wildcard $(SOURCES)))
TARGETNAME=OWASP Application Security Verification Standard 4.0

# Change LaTeX engine
PANDOC_MD_FLAGS=-f gfm -s -t markdown
PANDOC_PDF_FLAGS=-f markdown -s -t latex --pdf-engine=xelatex \
				 --table-of-contents \
				 --number-sections \
				 --variable mainfont="DejaVu Sans" \
				 --variable monofont="DejaVu Sans Mono" \
				 --template ./templates/eisvogel.tex
#				 --variable fontsize=11pt \
#				 --variable geometry:"top=1.5cm, bottom=2.5cm, left=1.5cm, right=1.5cm" \
#				 --variable geometry:a4paper \

PANDOC_DOCX_FLAGS=-f markdown -s --reference-doc=./templates/reference.docx \
				  --columns 10000 -t docx

.PHONY: md $(BUILDDIR) pdf docx clean

all: $(TARGETS)	pdf docx

$(BUILDDIR): 
	@mkdir -p $(BUILDDIR)/en # make sure build dir exists

$(BUILDDIR)/en/%.md: $(BUILDDIR)
	sed -E 's#(\| ?)([0-9]{1,4})( ?\|)#\1[\2](https://cwe.mitre.org/data/definitions/\2.html)\3#' $(subst build,.,$@) > $@
	 


md: $(BUILDDIR)
	pandoc $(PANDOC_MD_FLAGS) -o $(BUILDDIR)/source.md $(BUILDDIR)/$(SOURCES) 
	sed -Ei 's#../images/#./images/#' $(BUILDDIR)/source.md

pdf: md
	pandoc $(PANDOC_PDF_FLAGS) -o "$(BUILDDIR)/$(TARGETNAME).pdf" $(BUILDDIR)/source.md

docx: md
	pandoc $(PANDOC_DOCX_FLAGS) -o "$(BUILDDIR)/$(TARGETNAME).docx" $(BUILDDIR)/source.md

clean:
	rm -rf $(BUILDDIR)/en
	rm $(BUILDDIR)/*.md
