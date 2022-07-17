import pulumi
import iam
import vpc
from pulumi_aws import eks

conf = pulumi.Config()

eks_cluster = eks.Cluster(
    'eks-cluster',
    name='eks-cluster',
    role_arn=iam.eks_role.arn,
    tags={
        'Name': 'eks-cluster',
    },
    vpc_config=eks.ClusterVpcConfigArgs(
        public_access_cidrs=['0.0.0.0/0'],
        security_group_ids=[vpc.eks_security_group.id],
        subnet_ids=vpc.subnet_ids,
    ),
)

eks_node_group = eks.NodeGroup(
    'eks-nodegroup',
    cluster_name=eks_cluster.name,
    node_group_name='eks-nodegroup',
    node_role_arn=iam.ec2_role.arn,
    instance_types=["t3.micro"],
    subnet_ids=vpc.subnet_ids,
    tags={
        'Name': 'cluster-nodegroup',
    },
    scaling_config=eks.NodeGroupScalingConfigArgs(
        desired_size=2,
        max_size=2,
        min_size=1,
    ),
)

### add ALB + ingress
### add Cloudflare records

pulumi.export('cluster-name', eks_cluster.name)
