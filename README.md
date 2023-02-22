# flaskProject
## task
- Create a customized Docker container from the current version of Python that deploys a simple python script.
- Push image to DockerHub, or Cloud based Container Registery (ECR)
- Project should deploy automatically to Kubernetes cluster
- Deployment should be to some form of Kubernetes service (can be hosted like Google Cloud Run or Amazon EKS, etc)

### Guide

#### Install the AWS CDK

`npm`Install using :

```shell
$ npm install -g aws-cdk
```

After the installation is complete, check `AWS CDK`the version :

```shell
cdk --version
```



#### Create a VPC

```python
vpc = ec2.Vpc.from_lookup(self, id='Vpc', is_default=True)
```

#### Create an IAM

```python
eks_master_role = iam.Role(self, 'EksMasterRole',
    role_name='EksAdminRole',
    assumed_by=iam.AccountRootPrincipal()
    )
```

#### Create EKS

```python
cluster = eks.Cluster(self, 
    'Cluster',  
    vpc=vpc, 
    version=eks.KubernetesVersion.V1_18, 
    masters_role=eks_master_role, 
    default_capacity=0  
    )
```

