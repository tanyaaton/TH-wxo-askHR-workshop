from ibm_watsonx_orchestrate.agent_builder.tools import tool
from ibm_watsonx_orchestrate.agent_builder.connections import ConnectionType
from ibm_watsonx_orchestrate.run import connections
import pandas as pd
import requests
import os
import uuid


MY_APP_ID="langflow_secret"

@tool(
  expected_credentials=[
    {"app_id": MY_APP_ID, "type": ConnectionType.KEY_VALUE}
  ]
)
def get_employee_leave_balance(user_query: str) -> str:
    """Retrieves employee information based on the provided employee ID.
    
    Args:
        employee_id (str): The employee's unique ID.
        
    Returns:
        A JSON string containing the employee's information.
    """
    creds = connections.key_value(MY_APP_ID)
    url = "https://aws-us-east-2.langflow.datastax.com/lf/1a574151-3fc5-448e-bf7e-d88fd4958c49/api/v1/run/1f6d3bed-ecf3-4f9a-9f67-154fbc68c2ba"  # The complete API endpoint URL for this flow

    # Request payload configuration
    payload = {
        "output_type": "chat",
        "input_type": "chat",
        "input_value": user_query
    }
    payload["session_id"] = str(uuid.uuid4())

    headers = { 
        "X-DataStax-Current-Org": creds.get("organization_id"), 
        "Authorization": "Bearer "+ creds.get("application_token"), 
        "Content-Type": "application/json", 
        "Accept": "application/json", 
    }

    try:
        # Send API request
        response = requests.request("POST", url, json=payload, headers=headers)
        response.raise_for_status()  # Raise exception for bad status codes

        # Print response
        print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
    except ValueError as e:
        print(f"Error parsing response: {e}")


