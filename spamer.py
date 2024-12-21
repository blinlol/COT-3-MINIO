from time import sleep
from minio import Minio, MinioAdmin
from minio.lifecycleconfig import LifecycleConfig, Rule
from minio.credentials.providers import EnvMinioProvider


cred = EnvMinioProvider()
client = Minio(
    endpoint="minio1:9000",
    credentials=cred,
    secure=False,
)
admin = MinioAdmin(
    endpoint="minio1:9000",
    credentials=cred,
    secure=False,
)
bucket = 'bt2'
quota_size = 50 * 1024 * 1024 # in bytes

# create bucket with quota
if not client.bucket_exists(bucket):
    client.make_bucket(bucket)
resp = admin.bucket_quota_set(bucket, quota_size)

# spam manuls
src_img = 'manul.jpg'
for i in range(4000):
    dst_img = f'{i}_manul.jpg'
    print(f"send {dst_img}")
    try:
        client.fput_object(bucket, dst_img, src_img, num_parallel_uploads=1)
        print(f'successfuly send {dst_img}')
    except Exception as e:
        print(f"error in fput_object: {e}")
        break