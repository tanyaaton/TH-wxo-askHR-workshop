set -x

orchestrate env activate trial-env
orchestrate tools import -k python -f tools/get_employee_leave_balance/get_employee_leave_balance.py -a langflow-app
orchestrate agents import -k native -f agents/langflow_agent.yml


