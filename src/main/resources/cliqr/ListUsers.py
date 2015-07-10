#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import sys
import com.xhaus.jyson.JysonCodec as json

print "Executing ListUsers.py"

if cliqrServer is None:
  print "No server provided"
  sys.exit(1)

request = HttpRequest(cliqrServer)
response = request.get('/v1/users')
httpStatusCode = response.status
print httpStatusCode
print response.response

if httpStatusCode == 200:
  print "Successful"
else:
  print "Error in listing users"
  sys.exit(1)
  
