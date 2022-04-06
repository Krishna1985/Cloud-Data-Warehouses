try:

vpc = ec2.Vpc(id=myClusterProps['VpcId'])

defaultSg = list(vpc.security_groups.all())[0]

print(defaultSg)

defaultSg.authorize_ingress(

GroupName=defaultSg.group_name,

CidrIp='0.0.0.0/0',

IpProtocol='TCP',

FromPort=int(DWH_PORT),

ToPort=int(DWH_PORT)

)

except Exception as e:

print(e)
