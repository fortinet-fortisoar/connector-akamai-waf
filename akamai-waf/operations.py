"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""
import json

import requests
from akamai.edgegrid import EdgeGridAuth
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger('akamai-waf')


class AkamaiWAF:
    def __init__(self, config):
        self.host = config.get('host')
        if not (self.host.startswith('https://') or self.host.startswith('http://')):
            self.server_url = 'https://' + self.host
        self.host = self.host.strip('/')
        self.access_token = config.get('access_token')
        self.client_token = config.get('client_token')
        self.client_secret = config.get('client_secret')
        self.verify_ssl = config.get('verify_ssl')

    def make_request(self, endpoint, method='GET', data=None, params=None, files=None):
        try:
            url = self.host + endpoint
            logger.info('Executing Akamai WAF url {}'.format(url))
            headers = {'Content-Type': 'application/json'}
            self.auth = EdgeGridAuth(client_token=self.client_token, client_secret=self.client_secret,
                                     access_token=self.access_token)

            # CURL UTILS CODE
            try:
                from connectors.debug_utils.curl_script import make_curl
                make_curl(method, endpoint, headers=headers, params=params, data=data, verify_ssl=self.verify_ssl)
            except Exception as err:
                logger.error(f"Error in curl utils: {str(err)}")

            response = requests.request(method, url, params=params, files=files, data=data, headers=headers,
                                        verify=self.verify_ssl, auth=self.auth)
            if response.ok:
                logger.info('Successfully got response for url {}'.format(url))
                return response.json()
            elif response.status_code == 400:
                error_response = response.json()
                raise ConnectorError(error_response)
            elif response.status_code == 401:
                error_response = response.json()
                raise ConnectorError(error_response)
            elif response.status_code == 404:
                error_response = response.json()
                raise ConnectorError(error_response)
            else:
                logger.error(response.json())
        except requests.exceptions.SSLError:
            logger.error('SSL certificate validation failed')
            raise ConnectorError('SSL certificate validation failed')
        except requests.exceptions.ConnectTimeout:
            logger.error('The request timed out while trying to connect to the server')
            raise ConnectorError('The request timed out while trying to connect to the server')
        except requests.exceptions.ReadTimeout:
            logger.error('The server did not send any data in the allotted amount of time')
            raise ConnectorError('The server did not send any data in the allotted amount of time')
        except requests.exceptions.ConnectionError:
            logger.error('Invalid endpoint or credentials')
            raise ConnectorError('Invalid endpoint or credentials')
        except Exception as err:
            logger.error(str(err))
            raise ConnectorError(str(err))
        raise ConnectorError(response.text)


def create_network_list(config: dict, params: dict):
    try:
        aw = AkamaiWAF(config)
        params = _build_payload(params)

        endpoint = f'/network-list/v2/network-lists'
        return aw.make_request(endpoint=endpoint, method='POST', data=json.dumps(params))
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


def get_network_list(config: dict, params: dict):
    try:
        aw = AkamaiWAF(config)
        params = _build_payload(params)

        endpoint = f'/network-list/v2/network-lists'
        return aw.make_request(endpoint=endpoint, method='GET', params=params)
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


def get_network_by_id(config: dict, params: dict):
    try:
        aw = AkamaiWAF(config)
        params = _build_payload(params)

        endpoint = f'/network-list/v2/network-lists/{params.pop("networkListId")}'
        return aw.make_request(endpoint=endpoint, method='GET', params=params)
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


def update_network_list(config: dict, params: dict):
    try:
        aw = AkamaiWAF(config)
        params = _build_payload(params)

        endpoint = f'/network-list/v2/network-lists/{params.pop("networkListId")}'
        qp = {"includeElements": params.pop("includeElements", False), "extended": params.pop("extended", False)}
        return aw.make_request(endpoint=endpoint, method='PUT', params=qp, data=json.dumps(params))
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


def delete_network_by_id(config: dict, params: dict):
    try:
        aw = AkamaiWAF(config)
        params = _build_payload(params)

        endpoint = f'/network-list/v2/network-lists/{params.pop("networkListId")}'
        return aw.make_request(endpoint=endpoint, method='DELETE', params=params)
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


def append_elements_to_network_list(config: dict, params: dict):
    try:
        aw = AkamaiWAF(config)
        params = _build_payload(params)

        endpoint = f'/network-list/v2/network-lists/{params.pop("networkListId")}/append'
        return aw.make_request(endpoint=endpoint, method='POST', data=json.dumps(params))
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


def delete_element_from_network_list(config: dict, params: dict):
    try:
        aw = AkamaiWAF(config)
        params = _build_payload(params)

        endpoint = f'/network-list/v2/network-lists/{params.pop("networkListId")}/append'
        return aw.make_request(endpoint=endpoint, method='DELETE', params=params)
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


def get_activation_status_of_network_list(config: dict, params: dict):
    try:
        aw = AkamaiWAF(config)
        params = _build_payload(params)

        endpoint = f'/network-list/v2/network-lists/{params.pop("networkListId")}/environments/{params.pop("environment")}/status'
        return aw.make_request(endpoint=endpoint, method='GET', params=params)
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


def activate_network_list(config: dict, params: dict):
    try:
        aw = AkamaiWAF(config)
        params = _build_payload(params)

        endpoint = f'/network-list/v2/network-lists/{params.pop("networkListId")}/environments/{params.pop("environment")}/activate'
        return aw.make_request(endpoint=endpoint, method='POST', data=json.dumps(params))
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


def _check_health(config):
    try:
        aw = AkamaiWAF(config)
        endpoint = "/network-list/v2/network-lists"
        response = aw.make_request(endpoint=endpoint)
        if response.ok:
            logger.info("Akamai WAF Connector Available")
            return True
        else:
            return False
    except Exception as err:
        logger.error(str(err))
        raise ConnectorError(str(err))


def _build_payload(params: dict, options_dict: dict = {}) -> dict:
    if params.get('list') and isinstance(params.get('list'), str):
        listElements = params.pop('list').split(',')
        params.update({'list': listElements})

    if params.get('notificationRecipients') and isinstance(params.get('notificationRecipients'), str):
        notificationRecipients = params.pop('notificationRecipients').split(',')
        params.update({'notificationRecipients': notificationRecipients})

    return {key: options_dict.get(val, val) if isinstance(val, str) else val for key, val in params.items() if
            isinstance(val, (bool, int)) or val}


operations = {
    "create_network_list": create_network_list,
    "get_network_list": get_network_list,
    "get_network_by_id": get_network_by_id,
    "update_network_list": update_network_list,
    "delete_network_by_id": delete_network_by_id,
    "append_elements_to_network_list": append_elements_to_network_list,
    "delete_element_from_network_list": delete_element_from_network_list,
    "get_activation_status_of_network_list": get_activation_status_of_network_list,
    "activate_network_list": activate_network_list,
}