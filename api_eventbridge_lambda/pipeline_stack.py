from constructs import Construct
from aws_cdk import ( 
Stack,
Environment,
SecretValue,
pipelines
)

from .webservice_stage import WebServiceStage

APP_ACCOUNT = '782160816199'

class PipelineStack(Stack):
  def __init__(self, scope: Construct, id: str, **kwargs):
    super().__init__(scope, id, **kwargs)

    source = pipelines.CodePipelineSource.git_hub("abhishekbose86/aws-apigw-lambda-eventbridge-kinesis-S3", "main",
        authentication=SecretValue.secrets_manager("github-token"))
    pipeline = pipelines.CodePipeline(self, 'Pipeline',
      pipeline_name='TestPipeline',

      synth=pipelines.ShellStep("Synth",
        input = source,
        commands=[
          'npm install -g aws-cdk && pip install -r requirements.txt',
          'pytest unittests',
          'cdk synth'
        ]
    ))

    pre_prod_app = WebServiceStage ( self, 'Pre-Prod',
     env = Environment (account = APP_ACCOUNT, region = "us-east-2" ))
    pipeline.add_stage(pre_prod_app)


