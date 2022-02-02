from custom_connector_integ_test.configuration import services
import time

# Use this method to poll flow executions.
def poll_for_execution_records_response(flow_name: str, execution_id: str, max_poll_time: int, time_between_polls: int):
    appflow = services.get_appflow()
    execution_record = None
    total_time = 0
    while True:
        time.sleep(time_between_polls)
        res = appflow.describe_flow_execution_records(flowName=flow_name)
        for record in res["flowExecutions"]:
            if record["executionId"] == execution_id:
                execution_record = record
                break
        total_time += time_between_polls
        if total_time > max_poll_time or (execution_record is not None and execution_record["executionStatus"] != "InProgress"):
            return execution_record
