                                                     AWS CROSS-REGION EBS BACKUP
OVERVIEW

An automated AWS backup and disaster recovery solution that creates EBS snapshots on a scheduled basis, copies them to a secondary AWS Region, and sends backup status notifications through Amazon SNS. This project automates EBS snapshot backup using AWS Lambda, Event Bridge Scheduler and SNS. The Amazon Event Bridge Scheduler triggers the lambda function at a scheduled time. The Lambda function evaluates and copies the snapshot to the destination region from source region. Amazon SNS is used to notify the status of the lambda function, while CloudWatch monitors lambda execution logs.

ARCHITECTURE

<img width="440" height="309" alt="image" src="https://github.com/user-attachments/assets/cf4588c4-2c0c-40fc-ba35-30b4461b8620" />
