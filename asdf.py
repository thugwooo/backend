from datetime import datetime, timedelta

now = datetime.now()
time_a = '2022-08-25T21:47:22.000'
time_b = '2022-08-25T23:47:22.000'
time_object_a = datetime.strptime(time_a, '%Y-%m-%dT%H:%M:%S.%f')
time_object_b = datetime.strptime(time_b, '%Y-%m-%dT%H:%M:%S.%f')
print(time_object_b-time_object_a >= timedelta(hours=2))
