import base64
import random
import string
import os

def sm_events_function(event, unused_context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    The printed value will be visible in Cloud Logging
    (https://cloud.google.com/functions/docs/monitoring/logging).

    Args:
          event (dict): Event payload.
          unused_context (google.cloud.functions.Context): Metadata for the event.
    """

    event_type = event['attributes']['eventType']
    print("event_type {}".format(event_type))
    if event_type == 'SECRET_UPDATE' or event_type == 'SECRET_VERSION_ADD':
      secret_id = event['attributes']['secretId']
      secret_metadata = base64.b64decode(event['data']).decode('utf-8')
      print('Secret {} was updated. Its new metadata is: {}'.format(secret_id, secret_metadata))
#     if event_type == 'SECRET_ROTATE':
      from google.cloud import secretmanager
      client = secretmanager.SecretManagerServiceClient()

      # REGION = os.environ.get('FUNCTION_REGION')      # us-central1
      project_id = os.environ.get('GCP_PROJECT')
      # FUNCTION_NAME = os.environ.get('FUNCTION_NAME') # test
      # IDENTITY = os.environ.get('FUNCTION_IDENTITY')  # PROJECT_ID@appspot.gserviceaccount.com

      # HOST = request.headers.get('Host')              # us-central1-PROJECT_ID.cloudfunctions.net
      # AUTHORIZATION = request.headers.get('Authorization')    # Bearer eyJh...
      # USER_AGENT = request.headers.get('User-Agent')  # Google-Cloud-Scheduler, Google-Cloud-Tasks

      # FUNCTION_MEMORY_MB = os.environ.get('FUNCTION_MEMORY_MB')       # 256
      # FUNCTION_TIMEOUT_SEC = os.environ.get('FUNCTION_TIMEOUT_SEC')

      parent = client.secret_path(project_id, secret_id)
      secret_id = event['attributes']['secretId']
      # Convert the string payload into a bytes. This step can be omitted if you
      # pass in bytes instead of a str for the payload argument.
      payload = get_random_string(12)
      payload = payload.encode("UTF-8")
      print('Payload {}'.format(payload))
      print('Secret {} is about to rotate'.format(secret_id))
      # Add the secret version.
      response = client.add_secret_version(
            request={"parent": parent, "payload": {"data": payload}}
      )
      # Print the new secret version name.
      print("Added secret version: {}".format(response.name))

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)
    return result_str
