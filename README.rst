=========
odnoklassniki
=========

::

This is a odnoklassniki.ru python API wrapper.

Installation
============

::

    $ pip install odnoklassniki

Usage
=====

::

    >>> import odnoklassniki
    >>> ok = odnoklassniki.Odnoklassniki(client_key, client_secret, access_token)
    >>> print ok.group.getInfo('uids'='your_group_id', 'fields'='members_count')
    1282