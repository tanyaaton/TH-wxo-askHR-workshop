orchestrate connections add -a langflow_secret
orchestrate connections configure -a langflow_secret --env draft -t team -k key_value
orchestrate connections configure -a langflow_secret --env live -t team -k key_value
orchestrate connections set-credentials \
  -a langflow_secret \
  --env draft \
  -e application_token= <YOUR_APPLICATION_TOKEN> \
  -e organization_id= <YOUR_ORGANIZATION_ID>