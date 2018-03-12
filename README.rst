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

.. image:: https://badges.gitter.im/alternativshik/python-odnoklassniki.svg
   :alt: Join the chat at https://gitter.im/alternativshik/python-odnoklassniki
   :target: https://gitter.im/alternativshik/python-odnoklassniki?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge