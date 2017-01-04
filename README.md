# dynamic-ip-aws-route53


## Install

    pip install dynamic-ip-aws-route53

## Usage

    dynamic-route53 --aws=my_aws_profile --hosted_zone=Z1BDYJDN34534 --domain=office.domain.com --ttl=600

## Help

    bash$ dynamic-route53 --help

    Usage: dynamic-route53 [options]

    Options:
      -h, --help            show this help message and exit
      -z HOSTED_ZONE,   --hosted_zone=HOSTED_ZONE
                            Route 53 Hosted Zone ID e.v. Z1674836123526
      -a AWS,           --aws=AWS
                            Set the AWS account from within the ~/.aws/credentials file
      -d DOMAIN,        --domain=DOMAIN
                            The subdomain to update, for example myrouter.domain.com
      -t TTL,           --ttl=TTL
                            The TTL to set on the record