Apigee - Python
===============

### NOT TESTED YES, STILL DEVELOPING ###

|pypi| |build| |coverage| |license|

In this repository, you'll find all the information about integrating Apigee with Python.


What is Apigee?
===============

Apigee helps you to:

* Interact with the apigee edge api

Create a free Apigee Account
============================

1. Go to `Apigee`_ and click Sign Up.

Installation
============

You can install the apigee Python SDK using the following command.

.. code-block::

    pip install apigee-python

For python3, use the following command

.. code-block::
    
    pip3 install apigee-python


Management SDK Usage
====================

To use the management library you will need to instantiate an Apigee object 

    from apigee_python.v1.organizations import Apis

    org_name = 'myorg'
    username = 'xxx'
    password = 'xxx'

    client = Apis(org_name, username, password)
    
    results = client.get()
    print(results)
