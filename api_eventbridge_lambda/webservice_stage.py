from aws_cdk import Stage
from constructs import Construct

from .api_eventbridge_lambda import ApiEventBridgeLambdaStack

class WebServiceStage(Stage):
  def __init__(self, scope: Construct, id: str, **kwargs):
    super().__init__(scope, id, **kwargs)

    service = ApiEventBridgeLambdaStack(self, 'WebService')

    self.url_output = service.url_output