FROM centos:7

MAINTAINER Kalemena

RUN yum install -y epel-release; \
    yum install -y python-pip python-devel gcc; \
    pip install zeroconf;
    
ADD [ "examples", "/examples" ]    

WORKDIR /examples

CMD ["bash"]
  

