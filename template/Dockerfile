FROM python:3.6
MAINTAINER @hohsiangwu <hohsiangwu@github.com>

# send SIGQUIT to stop container
STOPSIGNAL SIGQUIT

RUN touch /etc/inside-container

COPY . /{{ app_name }}
WORKDIR /{{ app_name }}

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        apt-transport-https \
        curl && \
    curl -s "http://packages.service.cp1-iad.github.net/pubkey.gpg" | apt-key add -

RUN echo "deb http://packages.service.cp1-iad.github.net/github-jessie jessie main" >> /etc/apt/sources.list ; \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        nginx=1.10.2+github1 && \
    rm -rf /var/lib/apt/lists/*

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE {{ port }}

CMD ["script/server"]
