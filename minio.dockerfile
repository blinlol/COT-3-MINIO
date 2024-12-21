FROM quay.io/minio/minio as minio
CMD [ "server", "/data", "--console-address", ":9001"]