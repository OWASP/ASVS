ARG CERT_FILE=none
ARG WITH_CERT=no
#First stage, start from alpine
FROM alpine:3 AS base
ENV DEBIAN_FRONTEND noninteractive

RUN apk add --update \
    alpine-sdk \
    fontconfig \
    font-noto-cjk \
    freetype \
    lua5.3 \
    perl \
    bash \
    python3  \
    libressl-dev \
    py3-pip \
    curl \
    gnupg \
    unzip \
    py3-certifi && \
    rm -rf /var/cache/apk/*

# Dockerfiles have no "if", then we need to create intermediate stages to match a variable
# These stages will setup necessary environment variables and copy custom CA authorities to
# your container. Helpful if within a corporate environment with an intercepting proxy, like e.g. Zscaler

FROM base AS base_yes
# use the CERT_FILE parameter passed as a build-arg
ARG CERT_FILE
ENV SSL_CERT_DIR=/usr/local/share/ca-certificates 
COPY ${CERT_FILE} $SSL_CERT_DIR/
RUN update-ca-certificates
# define environment variables
ENV HTTPS_CA_DIR=$SSL_CERT_DIR
ENV REQUESTS_CA_BUNDLE=$SSL_CERT_DIR/$CERT_FILE
ENV GIT_SSL_CAPATH=$REQUESTS_CA_BUNDLE
ENV GIT_SSL_CAINFO=$GIT_SSL_CAPATH
ENV CURL_CA_BUNDLE=$REQUESTS_CA_BUNDLE

FROM base AS base_no

#Install opentype fonts
FROM base_${WITH_CERT} as font_base

WORKDIR /fonts
ENV DEBIAN_FRONTEND noninteractive

#download fonts
RUN for font in source-sans source-serif source-code-pro; do \
	git_tarball_url="https://www.github.com/adobe-fonts/${font}"$(curl -L "https://github.com/adobe-fonts/${font}/tags" |  \
		     grep -o "/archive/refs/tags/.*\.zip" | grep -v 'variable' | sort -r | head -1 |tr -d '\n'); \
     echo "DOWNLOADING FROM: ${git_tarball_url}"; \
     curl -L --retry 5 "${git_tarball_url}" --output "$font.zip"; \
     unzip "${font}.zip" ; \
    done
RUN mkdir adobe-fonts
RUN find $PWD/ -name "*.ttf" -exec install -m644 {} adobe-fonts/ \; || return 1
RUN rm -rf $PWD/source*

FROM base_${WITH_CERT} as pandoc_base

#install python depencies
RUN pip install --upgrade pip
RUN pip install setuptools dicttoxml2

#install Pandoc
RUN adduser -s /bin/bash -g "pandoc" -D pandoc

RUN curl --output /tmp/pandoc.tar.gz -L https://github.com/jgm/pandoc/releases/download/2.19.2/pandoc-2.19.2-linux-amd64.tar.gz \
            && tar xvzf /tmp/pandoc.tar.gz --strip-components 1 -C /usr/local/ \
            && rm /tmp/pandoc.tar.gz

# verify pandoc installed correctly
RUN pandoc --version

# install as pandoc
USER pandoc

# setup workdir
WORKDIR /home/pandoc

# Install Lua Filters for pandoc
RUN curl --output /tmp/lua-filters.tar.gz -L https://github.com/pandoc/lua-filters/releases/latest/download/lua-filters.tar.gz  \
    && mkdir /home/pandoc/.pandoc \
    && tar xzf /tmp/lua-filters.tar.gz --strip-components=1 --one-top-level=/home/pandoc/.pandoc/ \
    && rm /tmp/lua-filters.tar.gz

FROM pandoc_base as tinytex_base
#Install tinyTex

# setup path
ENV PATH=/home/pandoc/.TinyTeX/bin/x86_64-linuxmusl/:$PATH
ENV TINY_TEX_VERSION=v0.45
RUN curl -L "https://raw.githubusercontent.com/rstudio/tinytex/${TINY_TEX_VERSION}/tools/install-bin-unix.sh" | sed -e 's/wget -qO-/curl -sL/' -e "s#\(sh -s\)#sed 's/wget/curl -LO/' | \1#" -e 's/retry-connrefused/tries 20/' > "install-unx.sh" \
	&& chmod +x install-unx.sh
RUN bash -c "./install-unx.sh" && rm install-unx.sh

FROM tinytex_base as latex_base

# add tlmgr to path
RUN /home/pandoc/.TinyTeX/bin/*/tlmgr path add

# verify tlmgr version and add packages needed to build the documents
RUN tlmgr --version 
RUN tlmgr update -self
RUN tlmgr install \
    xecjk \
    ctex \
    fancyhdr \
    ragged2e \
    koma-script \
    setspace \
    colortbl \
    footnotebackref \
    polyglossia \
    pagecolor \
    csquotes \
    caption \
    mdframed \
    needspace \
    titling \
    bookmark \
    newunicodechar \
    adjustbox \
    collectbox \
    listings \
    adjustbox \
    background \
    bidi \
    everypage \
    footmisc \
    fvextra \
    ly1 \
    mweights \
    pagecolor \
    titling \
    ucharcat \
    ulem \
    upquote \
    xurl \
    zref 

FROM latex_base as work_layer
#copy fonts from font_base
USER root
COPY --from=font_base /fonts/adobe-fonts /usr/share/fonts/opentype/adobe-fonts
RUN fc-cache -f -v "/usr/share/fonts/opentype/adobe-fonts"
USER pandoc

RUN tlmgr info --list

#setup the working dir for running make and creating the files
WORKDIR /data
VOLUME /data

#setup default action
ENTRYPOINT ["/scripts/run.sh"]
