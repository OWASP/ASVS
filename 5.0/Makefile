PROJDIR=$(realpath $(CURDIR))
BUILDDIR=build
DISTDIR=dist
TOOLSDIR=tools
TEMPLATEDIR=templates
TARGETNAME=OWASP_Application_Security_Verification_Standard-5_

LANGDIRS=en #fr
# Add the language directories to the project directory
# Create build and dist directories and language subdirectories
BUILDDIR=$(PROJDIR)/build
DISTDIR=$(PROJDIR)/dist
SOURCEDIR=$(PROJDIR)/src

SOURCE_FOLDERS := $(foreach lang, $(LANGDIRS), $(SOURCEDIR)/$(lang))
BUILD_FOLDERS := $(foreach lang, $(LANGDIRS), $(BUILDDIR)/$(lang))
DIST_FOLDERS := $(foreach lang, $(LANGDIRS), $(DISTDIR)/$(lang))
SOURCE_FILES := $(shell find $(SOURCEDIR) -type f -name "*.md")
BUILD_FILES := $(patsubst $(SOURCEDIR)/%, $(BUILDDIR)/%, $(SOURCE_FILES))

MD_FILES := $(foreach lang, $(LANGDIRS), $(DISTDIR)/$(lang)/source_$(lang).md)
PDF_FILES := $(foreach lang, $(LANGDIRS), $(DISTDIR)/$(lang)/$(TARGETNAME)$(lang).pdf)
TEX_FILES := $(foreach lang, $(LANGDIRS), $(DISTDIR)/$(lang)/$(TARGETNAME)$(lang).tex)
DOCX_FILES := $(foreach lang, $(LANGDIRS), $(DISTDIR)/$(lang)/$(TARGETNAME)$(lang).docx)
ODT_FILES := $(foreach lang, $(LANGDIRS), $(DISTDIR)/$(lang)/$(TARGETNAME)$(lang).odt)
JSON_FILES := $(foreach lang, $(LANGDIRS), $(DISTDIR)/$(lang)/$(TARGETNAME)$(lang).json)
JSON_FLAT_FILES := $(foreach lang, $(LANGDIRS), $(DISTDIR)/$(lang)/$(TARGETNAME)$(lang).flat.json)
CSV_FILES := $(foreach lang, $(LANGDIRS), $(DISTDIR)/$(lang)/$(TARGETNAME)$(lang).csv)
XML_FILES := $(foreach lang, $(LANGDIRS), $(DISTDIR)/$(lang)/$(TARGETNAME)$(lang).xml)

#TARGETS=$(addprefix $(DISTDIR)/,$(wildcard $(SOURCES)))
TARGETS=$(addprefix $(BUILDDIRS)/,$(wildcard $(SOURCE_FILES)))
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

.PHONY: md pdf docx json json_flat csv xml odt tex clean rm-build rm-dist

all: $(TARGETS)	pdf docx json json_flat csv xml rm-build

$(BUILDDIR):
	mkdir -p $@

$(DISTDIR):
	mkdir -p $@

# transform origin md files. needed by the next stages
$(BUILDDIR)/%.md: $(SOURCE_FILES) $(BUILD_FOLDERS) $(BUILDDIR)
	sed -E 's#(\| ?)([0-9]{1,4})( ?\|)#\1[\2](https://cwe.mitre.org/data/definitions/\2.html)\3#; s#^(\| :?---:? \| :?)---( .*)#\| :-----: \| :---------------------------------------------------\2#; s#.(./images/)#\1#; s#(\\)([rntv])#\\escape{\2}#g' $(patsubst $(BUILDDIR)/%, $(SOURCEDIR)/%, $@) > $@

$(DIST_FOLDERS): $(DISTDIR)
	echo $@
	mkdir -p $@

$(BUILD_FOLDERS): $(BUILDDIR)
	echo $@
	mkdir -p $@
	 
$(MD_FILES): $(BUILD_FILES) $(DIST_FOLDERS) $(BUILD_FOLDERS)
	mkdir -p $(@D)
	pandoc $(PANDOC_MD_FLAGS) -o $@ $(patsubst $(DISTDIR)/%, $(BUILDDIR)/%, $@)
	sed -Ei 's#../images/#./images/#' $@
md: $(MD_FILES)
	echo $(MD_FILES)

$(PDF_FILES): $(BUILD_FOLDERS) $(TARGETS) $(DIST_FOLDERS) transform-md
	pandoc $(PANDOC_PDF_FLAGS) --include-in-header=$(TEMPLATEDIR)/header-eisvogel.tex -o $@ --template $(TEMPLATEDIR)/eisvogel.tex $(subst dist,build,$(@D)/*.md) $(subst dist,src,$(@D)/0x00-Header.yaml)
pdf: $(PDF_FILES)

$(TEX_FILES): $(BUILD_FOLDERS) $(TARGETS) $(DIST_FOLDERS)
	pandoc $(PANDOC_TEX_FLAGS) --include-in-header=$(TEMPLATEDIR)/header-eisvogel.tex -o $@ --template $(TEMPLATEDIR)/eisvogel.tex $(subst dist,build,$(@D)/*.md) $(subst dist,src,$(@D)/0x00-Header.yaml)
tex: $(TEX_FILES)

$(DOCX_FILES): $(BUILD_FOLDERS) $(TARGETS) $(DIST_FOLDERS)
	pandoc $(PANDOC_DOCX_FLAGS) -o $@ $(subst dist,build,$(@D)/*.md) $(subst dist,src,$(@D)/0x00-Header.yaml)
docx: $(DOCX_FILES)

$(ODT_FILES): $(BUILD_FOLDERS) $(TARGETS) $(DIST_FOLDERS)
	pandoc $(PANDOC_ODT_FLAGS) -o $@ $(subst dist,build,$(@D)/*.md) --metadata-file=$(SOURCEDIR)/0x00-Header.yaml
odt: $(ODT_FILES)

$(JSON_FILES): $(SOURCE_FOLDERS) $(DIST_FOLDERS)
	python3 $(EXPORT_TOOL) --format json --language "$(subst dist,src,$(@D))" > $@
json: $(JSON_FILES)

$(JSON_FLAT_FILES): $(SOURCE_FOLDERS) $(DIST_FOLDERS)
	python3 $(EXPORT_TOOL) --format json_flat --language "$(subst dist,src,$(@D))" > $@
json_flat: $(JSON_FLAT_FILES)

$(CSV_FILES): $(SOURCE_FOLDERS) $(DIST_FOLDERS)
	python3 $(EXPORT_TOOL) --format csv --language "$(subst dist,src,$(@D))" > $@
csv: $(CSV_FILES)

$(XML_FILES): $(SOURCE_FOLDERS) $(DIST_FOLDERS)
	python3 $(EXPORT_TOOL) --format xml --language "$(subst dist,src,$(@D))" > $@
xml: $(XML_FILES)

rm-build: $(BUILDDIR)
	rm -rf $(BUILDDIR)

rm-dist: $(DIST_FOLDERS)
	rm -rf $(DIST_FOLDERS)

clean: rm-build rm-dist

transform-md: $(BUILD_FILES)
