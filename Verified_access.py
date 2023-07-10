# std
import logging
import re
import sys
from typing import (
    Union,
    Optional,
    Dict,
    Literal,
    Any
)

# cdk
from aws_cdk import (
    CfnOutput, RemovalPolicy,
    Stack,
    ArnFormat,
    Fn,
    aws_logs as _logs,
    aws_ssm as _ssm,
    aws_ec2 as _ec2
)
from constructs import Construct

class VerifiedAccessInstance(Construct):

        def __init__(self, scope: Construct, construct_id: str) -> None:
            super().__init__(scope, construct_id)

            @staticmethod
            def _verifiedAccessLogsProperties(log_group_name: str):
                """Define Verified Access Logging Properties
                
                :param enabled bool [True|False]
                :param log_group String
                :return: AWS CDK Verified Access Instance Log Group
                
                """
                return _ec2.CfnVerifiedAccessInstance.verifiedAccessLogsProperties(
                    log_group = _logs.LogGroup(
                        self,
                        id='verified_access_log_group',
                        log_group_name=log_group_name,
                    )

                )