#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from hipchat.Hipchat import HipchatClient

hipchat = HipchatClient.get_client(hipchat_authentication)
method = str(task.getTaskType()).lower().replace('.', '_')
call = getattr(hipchat, method)
output = call(locals())