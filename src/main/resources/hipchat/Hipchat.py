#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import json, requests

class HipchatClient(object):
    def __init__(self, hipchat_authentication):
        self.url = hipchat_authentication["url"]
        self.headers = {
            'Content-Type' : 'application/json',
            'Authorization' : 'Bearer %s' % hipchat_authentication["api_access_token"]
        }

    @staticmethod
    def get_client(hipchat_authentication):
        return HipchatClient(hipchat_authentication)

    def notify(self, type, id, message):
        message_json='{"message":"%s","notify":"true"}' % message
        return self.get_response_for_endpoint('POST', type, 'Could not perform operation for [%s]' % id, data=message_json)

    def hipchat_notifyroom(self, variables):
        return self.notify('room/%s/notification' % variables['room_id'], variables['room_id'], variables['message'])

    def hipchat_messageuser(self, variables):
        return self.notify('user/%s/message' % variables['user_id'], variables['user_id'], variables['message'])

    def open_url(self, method, url, headers=None, data=None, json_data=None):
        if headers is None:
            headers = self.headers
        print "url : %s" % url
        return requests.request('%s' % method, url, data=data, json=json_data, headers=headers, verify=False)

    def get_response_for_endpoint(self, method, endpoint, error_message, object_id=None, json_data=None, data=None, headers=None):
        full_endpoint_url = "%s/%s" % (self.url, endpoint)
        if object_id is not None and object_id:
            full_endpoint_url = "%s/%s" % (full_endpoint_url, object_id)
        response = self.open_url(method, full_endpoint_url, headers=headers, json_data=json_data, data=data)
        if not response.ok:
            raise Exception(error_message)
        return response.text
