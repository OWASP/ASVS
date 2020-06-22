BUILDDIR=build
TOOLSDIR=tools
SOURCEDIR=en
SOURCES = $(SOURCEDIR)/*.md
TARGETNAME=OWASP Application Security Verification Standard 4.0

# Change LaTeX engine
PARAMETERS=--pdf-engine=xelatex
PANDOC_MD_FLAGS=-f gfm -s -t markdown
PANDOC_PDF_FLAGS=-f markdown -s -t latex

.PHONY: md $(BUILDDIR) pdf

all: pdf

$(BUILDDIR): 
	@mkdir -p $(BUILDDIR) # make sure build dir exists

# pandoc -s -f gfm --reference-doc=../templates/reference.docx --columns 10000 -t docx -o "../OWASP Application Security Verification Standard 4.0-$1.docx" *.md
md: $(BUILDDIR)
	@mkdir -p $(BUILDDIR) # make sure build dir exists
	pandoc $(PANDOC_MD_FLAGS) -o $(BUILDDIR)/source.md $(SOURCES) 

pdf: md
	pandoc $(PARAMETERS) $(PANDOC_PDF_FLAGS) -o "$(BUILDDIR)/$(TARGETNAME).pdf" $(BUILDDIR)/source.md
