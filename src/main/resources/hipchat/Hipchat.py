#
#
# Copyright 2018 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import json, requests, urllib

class HipchatClient(object):
    def __init__(self, hipchat_authentication):
        self.url = hipchat_authentication["url"]
        self.api_access_token = hipchat_authentication["api_access_token"]
        self.headers = {
            'Content-Type' : 'application/json',
            'Authorization' : 'Bearer %s' % hipchat_authentication["api_access_token"]
        }

    @staticmethod
    def get_client(hipchat_authentication):
        return HipchatClient(hipchat_authentication)

    def notify(self, type, id_or_name_list, end, message, color):
        message_json='{"message":%s,"notify":"true","color":"%s"}' % (json.dumps(message), color)

        for id_or_name in id_or_name_list:
            self.get_response_for_endpoint('POST', '%s/%s/%s' % (type, urllib.quote(id_or_name), end), 'Could not perform operation for [%s].' % id, data=message_json)

    def hipchat_notifyroom(self, variables):
        rooms = variables['rooms']

        # Add the single room_id if it exists (deprecated field)
        if variables['room_id']:
            rooms += [variables['room_id']]

        self.notify('room', rooms, 'notification', variables['message'],
                           variables['color'])

    def hipchat_messageuser(self, variables):
        users = variables['users']

        # Add the single user_id if it exists (deprecated field)
        if variables['user_id']:
            users += [variables['user_id']]

        self.notify('user', users, 'message', variables['message'],
                           variables['color'])

    def open_url(self, method, url, headers=None, data=None, json_data=None):
        if headers is None:
            headers = self.headers
        return requests.request('%s' % method, url, data=data, json=json_data, headers=headers, verify=False)

    def get_response_for_endpoint(self, method, endpoint, error_message, object_id=None, json_data=None, data=None, headers=None):
        full_endpoint_url = "%s/%s" % (self.url, endpoint)
        if object_id is not None and object_id:
            full_endpoint_url = "%s/%s" % (full_endpoint_url, object_id)
        response = self.open_url(method, full_endpoint_url, headers=headers, json_data=json_data, data=data)
        if not response.ok:
            raise Exception("%s [%s: %s]" % (error_message, response.status_code, response.text))
        return response.text

    def test_connection(self):
        return self.get_response_for_endpoint("GET", "oauth/token/%s" % self.api_access_token, "Could not retrieve basic information from HipChat with Authentication provided.")
