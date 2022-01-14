FROM alpine:latest

RUN apk --update --upgrade add bash cairo pango gdk-pixbuf py3-cffi py3-pillow py3-pip gcc g++ libxml2-dev libxslt-dev zopfli python3-dev musl-dev

RUN pip3 install weasyprint gunicorn flask lxml

RUN mkdir /documentbuilder
WORKDIR /documentbuilder
ADD ./wsgi.py /documentbuilder
RUN mkdir /root/.fonts
ADD ./fonts/* /root/.fonts/

CMD gunicorn --bind 0.0.0.0:5001 wsgi:app
