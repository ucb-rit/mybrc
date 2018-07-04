# Summary of REST Interface

## Root

### GET    /

```
HTTP/1.0 200 OK
Date: Tue, 05 Jun 2018 21:07:37 GMT
Server: WSGIServer/0.2 CPython/3.5.1
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Content-Length: 125
{
    "users":"http://128.3.7.72:8111/users/",
    "jobs":"http://128.3.7.72:8111/jobs/",
    "accounts":"http://128.3.7.72:8111/accounts/"
}
```

**TODO: Find out if this request can return a 401 Unauthorized.**

## Jobs Class (Create-Read-Update-List)

### GET    /jobs

Success (200 OK):

```
[benjaminzhang@phoenix ~]$ curl -i http://128.3.7.72:8111/jobs/
HTTP/1.0 200 OK
Date: Tue, 05 Jun 2018 21:39:05 GMT
Server: WSGIServer/0.2 CPython/3.5.1
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Content-Length: 485

{
    "count":171609,
    "next":"http://128.3.7.72:8111/jobs/?page=2",
    "previous":null,
    "results":{
        "jobnumber":[16,17,27,28,55,56,64,65,68,69,79,80,88,89,94,95,98,99,102,103,104,105,116,117,124,125,132,133,134,135,146,147,154,155,164,165,183,184,191,192,194,195,199,200,211,212,213,214,222,223,228,229,233,234,238,239,242,243,278,279,293,294,297,298,308,309,316,317,326,327,328,329,333,334,349,350,365,366,392,393,395,396,399,400,402,403,406,407,413,414,428,429,432,433,438,439,440,441,448,449]
    }
}
```

**TODO: Add a `"success": true` field to this response.**

Failure (401 Unauthorized):

```
{
    success : false,
    error : “Not authorized.”
}
```

---

### GET    /jobs?slurmjobid={id}            int

### GET    /jobs?userid={id}                int

### GET    /jobs?accountid={id}                int

### GET    /jobs?status={id}                int

### GET    /jobs?amount={amount}            float

### GET    /jobs?partition={id}                int

### GET    /jobs?qos={id}                      int

### GET    /jobs?submitdate={date}              ISO_date_utc

### GET    /jobs?startdate={date}                ISO_date_utc

### GET    /jobs?enddate={date}                ISO_date_utc

### GET    /jobs?created={date}                ISO_date_utc

### GET    /jobs?updated={date}                ISO_date_utc

**Note: filtering with these parameters hasn't been implemented yet. These examples are taken from the doc "REST API Etc Info (Outdated)".**

Success (200 OK):
```
{
    success : true,
    _metadata: {
        page : 1, paginationcurrent : 100 ,paginationmax : 1000
    },
    jobs : [{id : 100}, {id : 5123}]
}
```

The `_metadata` field is questionable--pagination was overriden in the existing implementation, so instead of `_metadata` the query response will probably have the `next` and `previous` fields found in the `/jobs` endpoint in production.

Failure (400 Bad Request):

```
{
    success : false,
    error : “No jobs found with given {insert query here}.”
}
```

**TODO: this should probably be a 404 instead? Will have to ask Harrison/Sahil.**

Failure (401 Unauthorized):

```
{
    success : false,
    error : “Not authorized.”
}
```

---

### GET    /jobs/{id}                    int

Success (200 OK):

```
[benjaminzhang@phoenix ~]$ curl -i "http://128.3.7.72:8111/jobs/2/"
HTTP/1.0 200 OK
Date: Tue, 05 Jun 2018 23:37:11 GMT
Server: WSGIServer/0.2 CPython/3.5.1
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept, Cookie
Content-Length: 281
X-Frame-Options: SAMEORIGIN

{
    "jobnumber": 2,
    "jobslurmid": 1,
    "submitdate": "2017-07-18T08:39:29Z",
    "startdate": "2017-07-19T08:39:29Z",
    "enddate": "2017-07-20T08:39:29Z",
    "userid": 2,
    "accountid": 2,
    "amount": 2866850,
    "jobstatus": 4,
    "partition": 1,
    "qos": 18,
    "created": "2018-06-05T13:27:35Z",
    "updated": "2018-06-05T13:27:35Z"
}
```

**TODO: Add a `"success": true` field to this response.**

See the [database schema picture](./docs/db-schema.png) for the fields' types in the database (which are translated back and forth to JSON and validated by [ModelSerializer](http://www.django-rest-framework.org/api-guide/serializers/#modelserializer)).

Failure (400 Bad Request):

```
{
    success : false,
    error : “Invalid job/Job not found.”
}
```

Failure (401 Unauthorized):

```
{
    success : false,
    error : “Not authorized.”
}
```

---

### PATCH    /jobs/{id}                    int

This was originally `PUT` in the docs, but the default Django REST implementation uses `PATCH` instead. `PUT` would require all fields to be parameters.

Takes any number of arguments that match the model's fields, since `PATCH` corresponds to a partial update operation within Django REST. In practice, only used by the SLURM epilogue to adjust SU amount after the job finishes.

Success (200 OK):

```
[benjaminzhang@phoenix ~]$ curl -i -X PATCH -d amount=1337 "http://128.3.7.72:8111/jobs/2/"

HTTP/1.0 200 OK
Date: Tue, 05 Jun 2018 23:54:11 GMT
Server: WSGIServer/0.2 CPython/3.5.1
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept, Cookie
Content-Length: 278
X-Frame-Options: SAMEORIGIN

{
    "jobnumber": 2,
    "jobslurmid": 1,
    "submitdate": "2017-07-18T08:39:29Z",
    "startdate": "2017-07-19T08:39:29Z",
    "enddate": "2017-07-20T08:39:29Z",
    "userid": 2,
    "accountid": 2,
    "amount": 1337,
    "jobstatus": 4,
    "partition": 1,
    "qos": 18,
    "created": "2018-06-05T13:27:35Z",
    "updated": "2018-06-05T13:27:35Z"
}
```

**TODO: Add a `"success": true` field to this response.**

**TODO: Add logic to update the `updated` field on submission.**

Failure (400 Bad Request):

```
{
    success : false,
    error : “Invalid job/Job not found.”
}
```

Failure (400 Bad Request):

```
{
    success : false,
    error : “Invalid amount.”
}
```

Failure (401 Unauthorized):

```
{
    success : false,
    error : “Not authorized.”
}
```

### POST    /jobs

<pre>
[benjaminzhang@phoenix ~]$ curl -i -X OPTIONS "http://128.3.7.72:8111/jobs/"

HTTP/1.0 200 OK
Date: Wed, 13 Jun 2018 00:43:00 GMT
Server: WSGIServer/0.2 CPython/3.5.1
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept, Cookie
Content-Length: 1560
X-Frame-Options: SAMEORIGIN

{
    "name": "Job List",
    "description": "ViewSet for /api/jobs/",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ],
    "actions": {
        "POST": {
            "jobnumber": {
                "type": "integer",
                "required": false,
                "read_only": true,
                "label": "Jobnumber"
            },
            <b>"jobslurmid": {
                "type": "integer",
                "required": true,
                "read_only": false,
                "label": "Jobslurmid",
                "min_value": -2147483648,
                "max_value": 2147483647
            },
            "submitdate": {
                "type": "datetime",
                "required": true,
                "read_only": false,
                "label": "Submitdate"
            },</b>
            "startdate": {
                "type": "datetime",
                "required": false,
                "read_only": false,
                "label": "Startdate"
            },
            "enddate": {
                "type": "datetime",
                "required": false,
                "read_only": false,
                "label": "Enddate"
            },
            <b>"userid": {
                "type": "integer",
                "required": true,
                "read_only": false,
                "label": "Userid",
                "min_value": -2147483648,
                "max_value": 2147483647
            },
            "accountid": {
                "type": "integer",
                "required": true,
                "read_only": false,
                "label": "Accountid",
                "min_value": -2147483648,
                "max_value": 2147483647
            },
            "amount": {
                "type": "float",
                "required": true,
                "read_only": false,
                "label": "Amount"
            },
            "jobstatus": {
                "type": "integer",
                "required": true,
                "read_only": false,
                "label": "Jobstatus",
                "min_value": -2147483648,
                "max_value": 2147483647
            },
            "partition": {
                "type": "integer",
                "required": true,
                "read_only": false,
                "label": "Partition",
                "min_value": -2147483648,
                "max_value": 2147483647
            },
            "qos": {
                "type": "integer",
                "required": true,
                "read_only": false,
                "label": "Qos",
                "min_value": -32768,
                "max_value": 32767
            },</b>
            "created": {
                "type": "datetime",
                "required": false,
                "read_only": true,
                "label": "Created"
            },
            "updated": {
                "type": "datetime",
                "required": false,
                "read_only": true,
                "label": "Updated"
            }
        }
    }
}
</pre>

Required values bolded.

## Users Class (Create-Read-Update-List)

### GET    /users

Success (200 OK):

```
[benjaminzhang@phoenix ~]$ curl -i "http://128.3.7.72:8111/users/"

HTTP/1.0 200 OK
Date: Wed, 06 Jun 2018 00:44:22 GMT
Server: WSGIServer/0.2 CPython/3.5.1
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept, Cookie
Content-Length: 96
X-Frame-Options: SAMEORIGIN

{
    "count": 14,
    "next": null,
    "previous": null,
    "results": {
        "userid": [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14
        ]
    }
}
```

**TODO: Add a `"success": true` field to this response.**

Failure (401 Unauthorized):

```
{
    success : false,
    error : “Not authorized.”
}
```

---

### GET    /users?ldapid={id}                int

### GET    /users?accountid={id}                int

### GET    /users?saviousername={name}        string

### GET    /users?email={email}                string

### GET    /users?created={date}                ISO_date_utc

### GET    /users?updated={date}            ISO_date_utc

Same behavior as for jobs.

---

### GET    /users/{id}                    int

Success (200 OK):

```
[benjaminzhang@phoenix ~]$ curl -i "http://128.3.7.72:8111/users/1/"
HTTP/1.0 200 OK
Date: Wed, 06 Jun 2018 00:49:15 GMT
Server: WSGIServer/0.2 CPython/3.5.1
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept, Cookie
Content-Length: 192
X-Frame-Options: SAMEORIGIN

{
    "userid": 1,
    "accounts": [
        1,
        3
    ],
    "username": "shasan",
    "usermetadata": "despacito",
    "email": "shasan@ocf.berkeley.edu",
    "ldapuid": 1092385,
    "created": "2017-11-18T20:39:17Z",
    "updated": "2017-11-18T20:39:17Z"
}
```

**TODO: Add a `"success": true` field to this response.**

Again, see the [database schema picture](./docs/db-schema.png) for the fields' types in the database (which are translated back and forth to JSON and validated by [ModelSerializer](http://www.django-rest-framework.org/api-guide/serializers/#modelserializer)).

Failure (400 Bad Request):

```
{
    success : false,
    error : “Invalid user/User not found.”
}
```

Failure (401 Unauthorized):

```
{
    success : false,
    error : “Not authorized.”
}
```

---

### PATCH    /users/{uid}                    int

Used for updating a user.

Success (200 OK):

```
[benjaminzhang@phoenix ~]$ curl -i -X PATCH -d usermetadata=despacito "http://128.3.7.72:8111/users/1/"

HTTP/1.0 200 OK
Date: Wed, 06 Jun 2018 01:03:16 GMT
Server: WSGIServer/0.2 CPython/3.5.1
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept, Cookie
Content-Length: 194
X-Frame-Options: SAMEORIGIN

{
    "userid": 1,
    "accounts": [
        1,
        3
    ],
    "username": "shasan",
    "usermetadata": "despacito",
    "email": "shasan@ocf.berkeley.edu",
    "ldapuid": 1092385,
    "created": "2017-11-18T20:39:17Z",
    "updated": "{now}"
}
```

**TODO: Add a `"success": true` field to this response.**

**TODO: Implement logic so that the `updated` field changes.**

Failure (400 Bad Request):

```
{
    success : false,
    error : “Invalid user information.”
}
```

Failure (401 Unauthorized):

```
{
    success : false,
    error : “Not authorized.”
}
```

### POST    /users

<pre>
[benjaminzhang@phoenix ~]$ curl -i -X OPTIONS "http://128.3.7.72:8111/users/"

HTTP/1.0 200 OK
Date: Thu, 14 Jun 2018 23:32:29 GMT
Server: WSGIServer/0.2 CPython/3.5.1
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept, Cookie
Content-Length: 945
X-Frame-Options: SAMEORIGIN

{
    "name": "User List",
    "description": "ViewSet for /api/users/",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ],
    "actions": {
        "POST": {
            "userid": {
                "type": "integer",
                "required": false,
                "read_only": true,
                "label": "Userid"
            },
            "accounts": {
                "type": "field",
                "required": false,
                "read_only": true,
                "label": "Accounts"
            },
            <b>"username": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Username",
                "max_length": 20
            },
            "usermetadata": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Usermetadata"
            },
            "email": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Email",
                "max_length": 100
            },
            "ldapuid": {
                "type": "integer",
                "required": true,
                "read_only": false,
                "label": "Ldapuid",
                "min_value": -2147483648,
                "max_value": 2147483647
            },</b>
            "created": {
                "type": "datetime",
                "required": false,
                "read_only": true,
                "label": "Created"
            },
            "updated": {
                "type": "datetime",
                "required": false,
                "read_only": true,
                "label": "Updated"
            }
        }
    }
}
</pre>

Required values bolded.

Returns 200 OK, 400 Bad Request (Invalid information), or 401 Unauthorized

## Accounts Class (Create-Read-Update-List)

### GET    /accounts

Success (200 OK):

```
[benjaminzhang@phoenix ~]$ curl -i "http://128.3.7.72:8111/accounts/"

HTTP/1.0 200 OK
Date: Wed, 06 Jun 2018 01:14:03 GMT
Server: WSGIServer/0.2 CPython/3.5.1
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept, Cookie
Content-Length: 723
X-Frame-Options: SAMEORIGIN

{
    "count": 3,
    "next": null,
    "previous": null,
    "results": {
        "accountid": [
            1,
            2,
            3
        ]
    }
}
```

**TODO: Add a `"success": true` field to this response.**

Failure (401 Unauthorized):

```
{
    success : false,
    error : “Not authorized.”
}
```

---

### GET    /accounts?userid={userid}            int

### GET    /accounts?accountname={name}        string

### GET    /accounts?allocation={allocation}        int

### GET    /accounts?type={type}                string

### GET    /accounts?created={date}            ISO_date_utc

### GET    /accounts?updated={date}            ISO_date_utc

Same behavior as for jobs.

---

### GET    /accounts/{accountid}                int

Success (200 OK):

```
[benjaminzhang@phoenix ~]$ curl -i "http://128.3.7.72:8111/accounts/1/"

HTTP/1.0 200 OK
Date: Wed, 06 Jun 2018 01:17:00 GMT
Server: WSGIServer/0.2 CPython/3.5.1
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept, Cookie
Content-Length: 223
X-Frame-Options: SAMEORIGIN

{
    "accountid": 1,
    "users": [
        1,
        4
    ],
    "accountname": "fc_hasan",
    "accountallocation": 1000000,
    "accountbalance": 1000000,
    "type": "FCA",
    "description": "Research of potatoes",
    "created": "2018-06-05T13:27:34Z",
    "updated": "2018-06-05T13:27:34Z"
}
```

**TODO: Add a `"success": true` field to this response.**

Again, see the [database schema picture](./docs/db-schema.png) for the fields' types in the database (which are translated back and forth to JSON and validated by [ModelSerializer](http://www.django-rest-framework.org/api-guide/serializers/#modelserializer)).

Failure (400 Bad Request):

```
{
    success : false,
    error : “Invalid account/Account not found.”
}
```

Failure (401 Unauthorized):

```
{
    success : false,
    error : “Not authorized.”
}
```

---

### PATCH    /accounts/{aid}                int

Success (200 OK):

```
[benjaminzhang@phoenix ~]$ curl -i -X PATCH -d accountname=fc_zhang "http://128.3.7.72:8111/accounts/1/"

HTTP/1.0 200 OK
Date: Wed, 06 Jun 2018 01:22:07 GMT
Server: WSGIServer/0.2 CPython/3.5.1
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept, Cookie
Content-Length: 223
X-Frame-Options: SAMEORIGIN

{
    "accountid": 1,
    "users": [
        1,
        4
    ],
    "accountname": "fc_zhang",
    "accountallocation": 1000000,
    "accountbalance": 1000000,
    "type": "FCA",
    "description": "Research of potatoes",
    "created": "2018-06-05T13:27:34Z",
    "updated": "2018-06-05T13:27:34Z"
}
```

**TODO: Implement logic so that the `updated` field changes.**

**TODO: Add a `"success": true` field to this response.**

Failure (400 Bad Request):

```
{
    success : false,
    error : “Invalid account information.”
}
```

Failure (401 Unauthorized):

```
{
    success : false,
    error : “Not authorized.”
}
```

### POST    /accounts

<pre>
[benjaminzhang@phoenix ~]$ curl -i -X OPTIONS "http://128.3.7.72:8111/accounts/"                                                                                                                            
HTTP/1.0 200 OK
Date: Tue, 12 Jun 2018 23:23:11 GMT
Server: WSGIServer/0.2 CPython/3.5.1
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept, Cookie
Content-Length: 1131
X-Frame-Options: SAMEORIGIN

{
    "name": "Account List",
    "description": "ViewSet for /api/accounts/",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ],
    "actions": {
        "POST": {
            "accountid": {
                "type": "integer",
                "required": false,
                "read_only": true,
                "label": "Accountid"
            },
            "users": {
                "type": "field",
                "required": false,
                "read_only": true,
                "label": "Users"
            },
            <b>"accountname": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Accountname",
                "max_length": 50
            },
            "accountallocation": {
                "type": "integer",
                "required": true,
                "read_only": false,
                "label": "Accountallocation",
                "min_value": -2147483648,
                "max_value": 2147483647
            },
            "accountbalance": {
                "type": "integer",
                "required": true,
                "read_only": false,
                "label": "Accountbalance",
                "min_value": -2147483648,
                "max_value": 2147483647
            },
            "type": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Type",
                "max_length": 10
            },
            "description": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Description",
                "max_length": 150
            },</b>
            "created": {
                "type": "datetime",
                "required": false,
                "read_only": true,
                "label": "Created"
            },
            "updated": {
                "type": "datetime",
                "required": false,
                "read_only": true,
                "label": "Updated"
            }
        }
    }
}
</pre>

Required values bolded.

Returns 200 OK, 400 Bad Request (Invalid information), or 401 Unauthorized

# Authentication

Use OAuth 2 path to authenticate the client. (To be implemented)

# TODO List

* Add "success" fields to responses.
* Implement filtering.
* Do everything else.
* Catch invalid syntax errors and return a 404.
* Implement all `400 Bad Request` responses.