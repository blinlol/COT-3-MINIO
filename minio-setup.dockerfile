FROM alpine
WORKDIR /
RUN apk add --update && apk --no-cache add curl
RUN curl https://dl.min.io/client/mc/release/linux-amd64/mc --create-dirs -o /bin/mc
RUN chmod +x /bin/mc
COPY minio-setup.sh .
CMD [ "sh", "minio-setup.sh" ]
