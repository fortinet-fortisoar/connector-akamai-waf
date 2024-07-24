## About the connector
Akamai Web Application Firewall (WAF) is a cloud-based security solution designed to protect web applications from various cyber threats. It acts as a shield between internet traffic and web servers, inspecting incoming requests to detect and block malicious activities
<p>This document provides information about the Akamai WAF Connector, which facilitates automated interactions, with a Akamai WAF server using FortiSOAR&trade; playbooks. Add the Akamai WAF Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Akamai WAF.</p>

### Version information

Connector Version: 1.0.0

FortiSOAR&trade; Version Tested on: 7.4.1-3167

Authored By: Fortinet

Certified: No

## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-akamai-waf</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Akamai WAF server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Akamai WAF server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Akamai WAF</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Host URL</td><td>Specify the Host URL that you have generated via Akamai WAF Identity and Access Management. It can be found in your .edgerc file
</td>
</tr><tr><td>Access Token</td><td>Specify the Access Token that you have generated via Akamai WAF Identity and Access Management. It can be found in your .edgerc file
</td>
</tr><tr><td>Client Token</td><td>Specify the Client Token that you have generated via Akamai WAF Identity and Access Management. It can be found in your .edgerc file
</td>
</tr><tr><td>Client Secret</td><td>Specify the Client Secret that you have generated via Akamai WAF Identity and Access Management. It can be found in your .edgerc file
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Create Network List</td><td>Creates a new Network list on behalf of an authenticated user based on the parameters provided</td><td>create_network_list <br/>Investigation</td></tr>
<tr><td>Get Network List</td><td>Retrieves all network lists available for an authenticated user based on the parameters provided</td><td>get_network_list <br/>Investigation</td></tr>
<tr><td>Get Network by ID</td><td>Retrieves details of the Network lists based on the Network List ID and other parameters provided</td><td>get_network_by_id <br/>Investigation</td></tr>
<tr><td>Update Network List</td><td>Update details of the Network lists based on the Network List ID and other parameters provided</td><td>update_network_list <br/>Investigation</td></tr>
<tr><td>Delete Network by ID</td><td>Deletes a Network list based on the Network List ID and other parameters provided</td><td>delete_network_by_id <br/>Investigation</td></tr>
<tr><td>Append Elements to Network List</td><td>Appends a set of elements to a Network list based on the Network List ID and other parameters provided</td><td>append_elements_to_network_list <br/>Investigation</td></tr>
<tr><td>Delete an Element from Network List</td><td>Deletes an element from a Network list based on the Network List ID, Element and other parameters provided</td><td>delete_element_from_network_list <br/>Investigation</td></tr>
<tr><td>Activate Network List</td><td>Activates the most recent syncPoint version of a network list in either the STAGING or PRODUCTION environment.</td><td>activate_network_list <br/>Investigation</td></tr>
<tr><td>Get Activation Status of Network List</td><td>Shows a Network list's activation status on either the STAGING or PRODUCTION environment</td><td>get_activation_status_of_network_list <br/>Investigation</td></tr>
</tbody></table>

### operation: Create Network List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Name</td><td>Specify the Display name of the network list
</td></tr><tr><td>Type</td><td>Specify the Network list type, either IP for IP addresses and CIDR blocks, or GEO for two-letter country codes
</td></tr><tr><td>List of Elements</td><td>Specify the Elements (in a comma separated manner) to be added to the Network List
</td></tr><tr><td>Description</td><td>Specify the detailed Description of the Network List
</td></tr><tr><td>Contract ID</td><td>Specify the Contract ID where you want to create the list
</td></tr><tr><td>Group ID</td><td>Specify the Group ID where you want to create the list
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "shared": "",
    "name": "",
    "uniqueId": "",
    "syncPoint": "",
    "type": "",
    "networkListType": "",
    "contractId": "",
    "elementCount": "",
    "groupId": "",
    "readOnly": "",
    "list": [],
    "links": {
        "activateInProduction": {
            "href": "",
            "method": ""
        },
        "activateInStaging": {
            "href": "",
            "method": ""
        },
        "appendItems": {
            "href": "",
            "method": ""
        },
        "retrieve": {
            "href": ""
        },
        "statusInProduction": {
            "href": ""
        },
        "statusInStaging": {
            "href": ""
        },
        "update": {
            "href": "",
            "method": ""
        }
    }
}</pre>

### operation: Get Network List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Search</td><td>Specify the List items to search in response list, Only list items that matches the specified substring in any network list's will be returned
</td></tr><tr><td>List Type</td><td>Specify the list type with which you want to filter results. Filters the output to lists of only the given type of network lists if provided, either IP or GEO
</td></tr><tr><td>Extended</td><td>If enabled, provides additional response data identifying who created and updated the list and when, and the network list's deployment status in both STAGING and PRODUCTION environments. This data takes longer to provide.
</td></tr><tr><td>Include Elements</td><td>If enabled, the response list includes all items. For large network lists, this may slow responses and yield large response objects
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "links": {
        "create": {
            "href": "",
            "method": ""
        }
    },
    "networkLists": [
        {
            "networkListType": "",
            "accessControlGroup": "",
            "name": "",
            "elementCount": "",
            "readOnly": "",
            "shared": "",
            "syncPoint": "",
            "type": "",
            "uniqueId": "",
            "links": {
                "activateInProduction": {
                    "href": "",
                    "method": ""
                },
                "activateInStaging": {
                    "href": "",
                    "method": ""
                },
                "appendItems": {
                    "href": "",
                    "method": ""
                },
                "retrieve": {
                    "href": ""
                },
                "statusInProduction": {
                    "href": ""
                },
                "statusInStaging": {
                    "href": ""
                },
                "update": {
                    "href": "",
                    "method": ""
                }
            }
        }
    ]
}</pre>

### operation: Get Network by ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Network List ID</td><td>Specify the ID of Network List which you want to retrieve
</td></tr><tr><td>Extended</td><td>If enabled, provides additional response data identifying who created and updated the list and when, and the network list's deployment status in both STAGING and PRODUCTION environments. This data takes longer to provide.
</td></tr><tr><td>Include Elements</td><td>If enabled, the response list includes all items. For large network lists, this may slow responses and yield large response objects
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "shared": "",
    "name": "",
    "uniqueId": "",
    "syncPoint": "",
    "type": "",
    "networkListType": "",
    "contractId": "",
    "elementCount": "",
    "groupId": "",
    "readOnly": "",
    "list": [],
    "links": {
        "activateInProduction": {
            "href": "",
            "method": ""
        },
        "activateInStaging": {
            "href": "",
            "method": ""
        },
        "appendItems": {
            "href": "",
            "method": ""
        },
        "retrieve": {
            "href": ""
        },
        "statusInProduction": {
            "href": ""
        },
        "statusInStaging": {
            "href": ""
        },
        "update": {
            "href": "",
            "method": ""
        }
    }
}</pre>

### operation: Update Network List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Network List ID</td><td>Specify the ID of Network List which you want to retrieve
</td></tr><tr><td>Name</td><td>Specify the Display name of the network list
</td></tr><tr><td>Type</td><td>Specify the Network list type, either IP for IP addresses and CIDR blocks, or GEO for two-letter country codes
</td></tr><tr><td>List of Elements</td><td>Specify the Elements (in a comma separated manner) to be updated in the Network List
</td></tr><tr><td>Sync Point</td><td>Specify the Sync Point of the Network List. Sync Point identifies each version of the network list, which increments each time it's modified. You need to include this value in any requests to modify the list
</td></tr><tr><td>Description</td><td>Specify the detailed Description of the Network List
</td></tr><tr><td>Extended</td><td>If enabled, provides additional response data identifying who created and updated the list and when, and the network list's deployment status in both STAGING and PRODUCTION environments. This data takes longer to provide.
</td></tr><tr><td>Include Elements</td><td>If enabled, the response list includes all items. For large network lists, this may slow responses and yield large response objects
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "shared": "",
    "name": "",
    "uniqueId": "",
    "syncPoint": "",
    "type": "",
    "networkListType": "",
    "contractId": "",
    "elementCount": "",
    "groupId": "",
    "readOnly": "",
    "list": [],
    "links": {
        "activateInProduction": {
            "href": "",
            "method": ""
        },
        "activateInStaging": {
            "href": "",
            "method": ""
        },
        "appendItems": {
            "href": "",
            "method": ""
        },
        "retrieve": {
            "href": ""
        },
        "statusInProduction": {
            "href": ""
        },
        "statusInStaging": {
            "href": ""
        },
        "update": {
            "href": "",
            "method": ""
        }
    }
}</pre>

### operation: Delete Network by ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Network List ID</td><td>Specify the ID of Network List which you want to retrieve
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "status": "",
    "uniqueId": "",
    "syncPoint": ""
}</pre>

### operation: Append Elements to Network List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Network List ID</td><td>Specify the ID of Network List which you want to retrieve
</td></tr><tr><td>List of Elements</td><td>Specify the Elements (in a comma separated manner) to be added in the Network List
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "shared": "",
    "name": "",
    "uniqueId": "",
    "syncPoint": "",
    "type": "",
    "networkListType": "",
    "contractId": "",
    "elementCount": "",
    "groupId": "",
    "readOnly": "",
    "list": [],
    "links": {
        "activateInProduction": {
            "href": "",
            "method": ""
        },
        "activateInStaging": {
            "href": "",
            "method": ""
        },
        "appendItems": {
            "href": "",
            "method": ""
        },
        "retrieve": {
            "href": ""
        },
        "statusInProduction": {
            "href": ""
        },
        "statusInStaging": {
            "href": ""
        },
        "update": {
            "href": "",
            "method": ""
        }
    }
}</pre>

### operation: Delete an Element from Network List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Network List ID</td><td>Specify the ID of Network List which you want to retrieve
</td></tr><tr><td>Element Value</td><td>Specify the Elements to be deleted from the Network List
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "shared": "",
    "name": "",
    "uniqueId": "",
    "syncPoint": "",
    "type": "",
    "networkListType": "",
    "contractId": "",
    "elementCount": "",
    "groupId": "",
    "readOnly": "",
    "list": [],
    "links": {
        "activateInProduction": {
            "href": "",
            "method": ""
        },
        "activateInStaging": {
            "href": "",
            "method": ""
        },
        "appendItems": {
            "href": "",
            "method": ""
        },
        "retrieve": {
            "href": ""
        },
        "statusInProduction": {
            "href": ""
        },
        "statusInStaging": {
            "href": ""
        },
        "update": {
            "href": "",
            "method": ""
        }
    }
}</pre>

### operation: Activate Network List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Network List ID</td><td>Specify the ID of Network List which you want to retrieve
</td></tr><tr><td>Environment</td><td>Specify the Akamai network on which this list is activated: STAGING or PRODUCTION
</td></tr><tr><td>Element Value</td><td>Specify the Elements to be deleted from the Network List
</td></tr><tr><td>Comment</td><td>Specify the descriptive text to accompany the activation. This is reflected in the activation object's activationComments member
</td></tr><tr><td>Notify Recipients</td><td>Specify the List of email addresses of Control Center users who receive an email when activation of this list is complete. Don't add addresses to this list without the recipients' consent
</td></tr><tr><td>Siebel Ticket ID</td><td>Specify the Siebel Ticket ID, If the activation is linked to a Siebel ticket, this identifies the ticket
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "activationId": "",
    "activationComments": "",
    "activationStatus": "",
    "syncPoint": "",
    "uniqueId": "",
    "fast": "",
    "dispatchCount": "",
    "links": {
        "appendItems": {
            "href": "",
            "method": ""
        },
        "retrieve": {
            "href": ""
        },
        "statusInProduction": {
            "href": ""
        },
        "statusInStaging": {
            "href": ""
        },
        "syncPointHistory": {
            "href": ""
        },
        "update": {
            "href": "",
            "method": ""
        },
        "activationDetails": {
            "href": ""
        }
    }
}</pre>

### operation: Get Activation Status of Network List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Network List ID</td><td>Specify the ID of Network List whose activation status you want to retrieve
</td></tr><tr><td>Environment</td><td>Specify the Akamai network on which this list is activated: STAGING or PRODUCTION
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "activationId": "",
    "activationComments": "",
    "activationStatus": "",
    "syncPoint": "",
    "uniqueId": "",
    "fast": "",
    "dispatchCount": "",
    "links": {
        "appendItems": {
            "href": "",
            "method": ""
        },
        "retrieve": {
            "href": ""
        },
        "statusInProduction": {
            "href": ""
        },
        "statusInStaging": {
            "href": ""
        },
        "syncPointHistory": {
            "href": ""
        },
        "update": {
            "href": "",
            "method": ""
        },
        "activationDetails": {
            "href": ""
        }
    }
}</pre>
## Included playbooks
The `Sample - akamai-waf - 1.0.0` playbook collection comes bundled with the Akamai WAF connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Akamai WAF connector.

- Activate Network List
- Append Elements to Network List
- Create Network List
- Delete Network by ID
- Delete an Element from Network List
- Get Activation Status of Network List
- Get Network List
- Get Network by ID
- Update Network List

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.