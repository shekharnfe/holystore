##### Http requests ####
# GET   Retrieve the resource from database
# POST  Create resource on database
# PUT    update existing resource on database
#Patch   update partial details of resource
# DELETE delete existing resource from database
from os import times

from pyexpat.errors import codes

from webTable import data1

#URI
#example of uri https://reqres.in/api/users?page=2
               # ----------------|----------------
                #Host               #path parameters

                # After ? mark it is query parameter

################# Validations on response  ################
# status code
# time
# size data
# response body(json/xml)
# cookies
# headers


#http status codes
# 3 levels

# 1. 200  200 oK, 201 created, 202 Accepted, 203 Non-Authoritative Information , 204 No Content
#
# 2. 400 Bad request, 401 UnAuthorized, 403 Forbidden, 404 Not Found,409 Conflict
#
# 3. 500 Internal server error, 501 Not Implemented, 502 Bad Gateway, 503 Service Unavailable
    # 504 Gateway Timeout, 599 Network Timeout