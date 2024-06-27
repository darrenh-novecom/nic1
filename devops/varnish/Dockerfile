# syntax=docker/dockerfile:1
FROM varnish:7.4

LABEL maintainer="Darren Hennessy <darren.hennessy@novecom.com.au>" \
      org.label-schema.name="nic1-varnish" \
      org.label-schema.description="Novecom Information Centre Varnish image." \
      org.label-schema.vendor="Darren Hennessy"

COPY etc/varnish.vcl /etc/varnish/default.vcl
