=====
Pykka
=====

Pykka is a Python implementation of the `actor model
<https://en.wikipedia.org/wiki/Actor_model>`_. The actor model introduces some
simple rules to control the sharing of state and cooperation between execution
units, which makes it easier to build concurrent applications.

For details and code examples, see the `Pykka documentation
<https://www.pykka.org/>`_.

Pykka is available from PyPI. To install it, run::

    pip install pykka

Pykka works with CPython 2.7 and 3.4+, as well as PyPy 2.7 and 3.5.

Optional dependencies includes:

- `gevent <http://www.gevent.org/>`_, if you want to use gevent based actors
  from ``pykka.gevent``.

- `eventlet <https://eventlet.net/>`_, if you want to use eventlet based
  actors from ``pykka.eventlet``.


License
=======

Pykka is copyright 2010-2019 Stein Magnus Jodal and contributors.
Pykka is licensed under the `Apache License, Version 2.0
<https://www.apache.org/licenses/LICENSE-2.0>`_.


Project resources
=================

- `Documentation <https://www.pykka.org/>`_
- `Source code <https://github.com/jodal/pykka>`_
- `Issue tracker <https://github.com/jodal/pykka/issues>`_

.. image:: https://img.shields.io/pypi/v/Pykka.svg?style=flat
    :target: https://pypi.python.org/pypi/Pykka/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/travis/jodal/pykka/develop.svg?style=flat
    :target: https://travis-ci.org/jodal/pykka
    :alt: Travis CI build status

.. image:: https://img.shields.io/coveralls/jodal/pykka/develop.svg?style=flat
   :target: https://coveralls.io/r/jodal/pykka?branch=develop
   :alt: Test coverage
