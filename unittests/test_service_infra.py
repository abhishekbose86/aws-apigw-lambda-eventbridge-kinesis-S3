from aws_cdk import App
from api_eventbridge_lambda.api_eventbridge_lambda import ApiEventBridgeLambdaStack

def test_lambda_handler():
  # GIVEN
  app = App()

  # WHEN
  ApiEventBridgeLambdaStack(app, 'Stack')

  # THEN
  template = app.synth().get_stack_by_name('Stack').template
  functions = [resource for resource in template['Resources'].values()
               if resource['Type'] == 'AWS::Lambda::Function']

  assert len(functions) == 3
  assert functions[0]['Properties']['Handler'] == 'event_producer_lambda.lambda_handler'
  assert functions[1]['Properties']['Handler'] == 'event_consumer_lambda.lambda_handler'
  assert functions[3]['Properties']['Handler'] == 'event_consumer_lambda.lambda_handler'