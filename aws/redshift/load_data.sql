COPY appointments
FROM 's3://your-bucket-name/appointments.csv'
CREDENTIALS 'aws_iam_role=arn:aws:iam::<ACCOUNT-ID>:role/<REDSHIFT-ROLE>'
CSV
IGNOREHEADER 1;

COPY metrics
FROM 's3://your-bucket-name/metrics.csv'
CREDENTIALS 'aws_iam_role=arn:aws:iam::<ACCOUNT-ID>:role/<REDSHIFT-ROLE>'
CSV
IGNOREHEADER 1;
