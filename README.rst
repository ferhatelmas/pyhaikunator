==========
haikunator
==========

Heroku like random name generator.

There is an djective and a noun list and it generates random name joining them by user provided delimiter.

Install
-------

Just install using pip::

    $ pip install pyhaikunator


Usage
-----

.. code-block:: python

    from haikunator import Haikunator


    Haikunator.haikunate()  # <-- 'icy-dream-4198'
    # drop random token at the end
    Haikunator.haikunate(0)  # <-- 'quiet-tree'
    # supply a delimiter
    Haikunator.haikunate(delimiter='~')  # <-- 'shy-feather-4125'
    # drop random token and supply delimiter at the same time
    Haikunator.haikunate(0, ' ')  # <-- 'wandering glitter'
    # provide a larger range for random token at the end
    Haikunator.haikunate(100000, '🐮') # <-- spring🐮pine🐮71030

Tests
-----

Just run module::

    $ python haikunator.py


License
-------

MIT

