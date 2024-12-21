mc alias set minio http://minio1:9000 fedor best_password
mc ilm tier add minio minio MINIO_TIER --access-key fedor --secret-key best_password --bucket bt2-tier --endpoint http://minio-tier:9000
mc mb minio/bt2
mc ilm rule add minio/bt2 --transition-tier MINIO_TIER --transition-days 1