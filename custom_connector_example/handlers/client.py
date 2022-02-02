import urllib3

CONNECTION_TIMEOUT_SECS = 30
READ_TIMEOUT_SECS = 600

class SalesforceResponse:
    def __init__(self, status_code: int, response: str, error_reason: str):
        self.status_code = status_code
        self.response = response
        self.error_reason = error_reason

class HttpsClient:
    def __init__(self, access_token):
        timeout = urllib3.Timeout(connect=CONNECTION_TIMEOUT_SECS, read=READ_TIMEOUT_SECS)
        self.https_client = urllib3.PoolManager(timeout=timeout)
        self.access_token = access_token
        self.authorization_header = {'Authorization': 'Bearer ' + access_token}

    def rest_get(self, request_uri: str) -> SalesforceResponse:
        headers = self.authorization_header
        resp = self.https_client.request(method='GET',
                                         url=request_uri,
                                         headers=headers)
        return SalesforceResponse(status_code=resp.status,
                                  response=resp.data.decode('utf-8'),
                                  error_reason=resp.reason)

    def rest_post(self, request_uri: str, post_data: str) -> SalesforceResponse:
        headers = {**self.authorization_header, 'Accept-Encoding': 'gzip', 'Content-Type': 'application/json'}
        resp = self.https_client.request(method='POST',
                                         url=request_uri,
                                         headers=headers,
                                         body=post_data)
        return SalesforceResponse(status_code=resp.status,
                                  response=resp.data.decode('utf-8'),
                                  error_reason=resp.reason)

    def rest_patch(self, request_uri: str, patch_data: str) -> SalesforceResponse:
        headers = {**self.authorization_header, 'Accept-Encoding': 'gzip', 'Content-Type': 'application/json'}
        resp = self.https_client.request(method='PATCH',
                                         url=request_uri,
                                         headers=headers,
                                         body=patch_data)
        return SalesforceResponse(status_code=resp.status,
                                  response=resp.data.decode('utf-8'),
                                  error_reason=resp.reason)

    def rest_put(self, request_uri: str, put_data: str) -> SalesforceResponse:
        headers = {**self.authorization_header, 'Content-Type': 'text/csv'}
        resp = self.https_client.request(method='PUT',
                                         url=request_uri,
                                         headers=headers,
                                         body=put_data)
        return SalesforceResponse(status_code=resp.status,
                                  response=resp.data.decode('utf-8'),
                                  error_reason=resp.reason)

    def rest_delete(self, request_uri: str) -> SalesforceResponse:
        resp = self.https_client.request(method='DELETE',
                                         url=request_uri,
                                         headers=self.authorization_header)
        return SalesforceResponse(status_code=resp.status,
                                  response=resp.data.decode('utf-8'),
                                  error_reason=resp.reason)
