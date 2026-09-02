import boto3

def lambda_handler(event, context):
    source_region = "ap-south-1"
    destination_region = "ap-south-2"
    source_ec2 = boto3.client(
        "ec2",
        region_name=source_region
    )
    destination_ec2 = boto3.client(
        "ec2",
        region_name=destination_region
    )
    response = source_ec2.describe_snapshots(
        OwnerIds=["self"],
        Filters=[
            {
                "Name": "tag:Backup",
                "Values": ["true"]
            }
        ]
    )
    for snap in response["Snapshots"]:
        snap_id = snap["SnapshotId"]
        tags = snap.get("Tags", [])
        dr_enabled = any(
            tag["Key"] == "DisasterRecovery" and
            tag["Value"] == "true"
            for tag in tags
        )
        if dr_enabled:
            print(snap_id, "requires DR copy")
            response = destination_ec2.copy_snapshot(
                SourceRegion=source_region,
                SourceSnapshotId=snap_id,
                Description="Backup copy"
            )
            print(
                snap_id,
                "copy started:",
                response["SnapshotId"]
            )
        else:
            print(
                snap_id,
                "does not require DR copy"
            )
