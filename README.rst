====================
pylistshine
====================


This is app that deals with subscribe/unsubscribe in ListShine mailing list system.

Quick start guide:
------------------

1. install pylistshine
   pip install pylistshine

API
---

1. Subscribing users

    conn = pylistshine.LSConnection('<API_KEY>')
    contact = conn.contact(list_id=<CONTACT_LIST_UUID>)
    contact.subscribe(email='test@email.com', firstname='test').json()


2. Unsubscribing users

    conn = pylistshine.LSConnection('<API_KEY>')
    contact = conn.contact(list_id=<CONTACT_LIST_UUID>)
    contact.unsubscribe(email='test@email.com')


3. Fetching users that match email

    conn = pylistshine.LSConnection('<API_KEY>')
    contact = conn.contact(list_id=<CONTACT_LIST_UUID>)
    contact.list(email='test@email.com').json()


4. Fetching users from contactlist

    conn = pylistshine.LSConnection('<API_KEY>')
    contact = conn.contact(list_id=<CONTACT_LIST_UUID>)
    contact.list(email='test@email.com').json()


5. Fetching users from contactlist

    conn = pylistshine.LSConnection('<API_KEY>')
    contact = conn.contact(list_id=<CONTACT_LIST_UUID>)
    contact.list(email='test@email.com').json()


Merge Vars
----------

When you are subscribing contacts you can use merge vars.
Following merge vars are supported:
* firstname
* lastname
* company
* website
* phone
* city
* country
* custom
* custom2
* custom3
* custom3

Example
--------

To subscribe contact test@test.com with firstname "name" and lastname "surname"

    contact.subscribe(email='test@test.com', firstname='name', lastname='surname')
