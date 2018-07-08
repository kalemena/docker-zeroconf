FROM centos:7

MAINTAINER Kalemena

# Build-time metadata as defined at http://label-schema.org
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="Kalemena ZeroConf" \
      org.label-schema.description="Kalemena ZeroConf" \
      org.label-schema.url="private" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/kalemena/docker-zeroconf" \
      org.label-schema.vendor="Kalemena" \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0"

RUN yum install -y epel-release; \
    yum install -y python-pip python-devel gcc; \
    pip install zeroconf;
    
ADD [ "examples", "/examples" ]    

WORKDIR /examples

CMD ["bash"]
  

