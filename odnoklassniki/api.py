from hashlib import md5
import requests

API_URL = 'https://api.ok.ru/fb.do'
DEFAULT_TIMEOUT = 30


class OdnoklassnikiError(Exception):
    __slots__ = ["error"]

    def __init__(self, error_data):
        self.error = error_data
        Exception.__init__(self, str(self))

    @property
    def code(self):
        return self.error['code']

    @property
    def message(self):
        return self.error['text']

    @property
    def params(self):
        return self.error['params']

    @property
    def method(self):
        return self.error['method']

    def __str__(self):
        return "Error(code: '{code}', description: '{description}', method: '{method}', params: '{params}')".format(
            code=self.code,
            description=str(self.message),
            method=self.method,
            params=self.params
        )


class _API(object):

    def __init__(self, application_key, application_secret, token, data_format):
        self.application_key = application_key
        self.application_secret = application_secret
        self.token = token
        self.data_format = data_format
        self.secret = self._secret
        self._method = None

    def _get(self, method, **kwargs):
        status, response = self._request(method, **kwargs)
        if not (200 <= status <= 299):
            raise OdnoklassnikiError({
                'code': status,
                'text': 'HTTP error',
                'method': method,
                'params': kwargs,
            })
        if isinstance(response, dict) and "error_code" in response:
            raise OdnoklassnikiError({
                'code': response.get('error_code'),
                'text': response.get('error_msg'),
                'method': method,
                'params': kwargs,
            })

        return response

    def __getattr__(self, name):
        api = _API(
            application_key=self.application_key,
            application_secret=self.application_secret,
            token=self.token,
            data_format=self.data_format
        )
        # Create method name like 'friends.get' from api call od.friends.get()
        if self._method:
            api._method = self._method + '.' + name
        else:
            api._method = name
        return api

    def __call__(self, **kwargs):
        return self._get(self._method, **kwargs)

    def _signature(self, params):
        # oAuth2 http://apiok.ru/wiki/pages/viewpage.action?pageId=42476652
        keys = sorted(params.keys())
        param_str = ''.join(['{k}={v}'.format(k=key, v=params[key]) for key in keys])
        param_str += self.secret
        return md5(param_str.encode('utf-8')).hexdigest().lower()

    @property
    def _secret(self):
        return md5('{token}{secret}'.format(token=self.token,
                                            secret=self.application_secret).encode('utf-8')).hexdigest().lower()

    def _request(self, method, timeout=DEFAULT_TIMEOUT, **kwargs):

        params = {
            'application_key': self.application_key,
            'format': self.data_format,
            'method': method,
        }
        params.update(kwargs)
        sig = self._signature(params)
        params['sig'] = sig
        if self.token:
            params['access_token'] = self.token

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        try:
            req = requests.post(API_URL, data=params, headers=headers, timeout=timeout)
            return req.status_code, req.json()
        except requests.exceptions.RequestException:
            raise OdnoklassnikiError({
                'code': None,
                'text': "HTTP error",
                'method': method,
                'params': params,
            })


class Odnoklassniki(_API):

    def __init__(self, application_key=None, application_secret=None, token=None):
        if not (application_key or application_secret or token):  # None or empty string
            raise ValueError('Api key required')
        _API.__init__(self, application_key=application_key,
                      application_secret=application_secret,
                      token=token, data_format='json')
