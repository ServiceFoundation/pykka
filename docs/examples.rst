========
Examples
========

The ``examples/`` dir in `Pykka's Git repo
<https://github.com/jodal/pykka/>`_ includes some runnable examples of Pykka
usage.


Plain actor
===========

.. literalinclude:: ../examples/plain_actor.py

Output::

    [{'no': 'Norway', 'se': 'Sweden'}, {'a': 3, 'b': 4, 'c': 5}]


Actor with proxy
================

.. literalinclude:: ../examples/typed_actor.py

Output::

    MainThread: calling AnActor.proc() ...
    MainThread: calling AnActor.func() ...
    MainThread: printing result ... (blocking)
    AnActor-1: this was printed by AnActor.proc()
    MainThread: this was returned by AnActor.func() after a delay
    MainThread: reading AnActor.field ...
    MainThread: printing result ... (blocking)
    MainThread: this is the value of AnActor.field
    MainThread: writing AnActor.field ...
    MainThread: printing new field value ... (blocking)
    MainThread: new value
    MainThread: calling AnActor.proc() ...
    MainThread: calling AnActor.func() ...
    MainThread: printing result ... (blocking)
    AnActor-1: this was printed by AnActor.proc()
    MainThread: this was returned by AnActor.func() after a delay
    MainThread: reading AnActor.field ...
    MainThread: printing result ... (blocking)
    MainThread: new value
    MainThread: writing AnActor.field ...
    MainThread: printing new field value ... (blocking)
    MainThread: new value
    MainThread: calling AnActor.proc() ...
    MainThread: calling AnActor.func() ...
    AnActor-1: this was printed by AnActor.proc()
    MainThread: printing result ... (blocking)
    MainThread: this was returned by AnActor.func() after a delay
    MainThread: reading AnActor.field ...
    MainThread: printing result ... (blocking)
    MainThread: new value
    MainThread: writing AnActor.field ...
    MainThread: printing new field value ... (blocking)
    MainThread: new value


Multiple cooperating actors
===========================

.. literalinclude:: ../examples/counter.py

Output::

    Adder (urn:uuid:f50029eb-7cea-4ab9-98bf-a5bf65af8b8f) is increasing 0
    Bookkeeper (urn:uuid:4f2d4e78-7a33-4c4f-86ac-7c415a7205f4) got 1 back
    Adder (urn:uuid:f50029eb-7cea-4ab9-98bf-a5bf65af8b8f) is increasing 1
    Bookkeeper (urn:uuid:4f2d4e78-7a33-4c4f-86ac-7c415a7205f4) got 2 back
    Adder (urn:uuid:f50029eb-7cea-4ab9-98bf-a5bf65af8b8f) is increasing 2
    Bookkeeper (urn:uuid:4f2d4e78-7a33-4c4f-86ac-7c415a7205f4) got 3 back
    Adder (urn:uuid:f50029eb-7cea-4ab9-98bf-a5bf65af8b8f) is increasing 3
    Bookkeeper (urn:uuid:4f2d4e78-7a33-4c4f-86ac-7c415a7205f4) got 4 back
    Adder (urn:uuid:f50029eb-7cea-4ab9-98bf-a5bf65af8b8f) is increasing 4
    Bookkeeper (urn:uuid:4f2d4e78-7a33-4c4f-86ac-7c415a7205f4) got 5 back
    Adder (urn:uuid:f50029eb-7cea-4ab9-98bf-a5bf65af8b8f) is increasing 5
    Bookkeeper (urn:uuid:4f2d4e78-7a33-4c4f-86ac-7c415a7205f4) got 6 back
    Adder (urn:uuid:f50029eb-7cea-4ab9-98bf-a5bf65af8b8f) is increasing 6
    Bookkeeper (urn:uuid:4f2d4e78-7a33-4c4f-86ac-7c415a7205f4) got 7 back
    Adder (urn:uuid:f50029eb-7cea-4ab9-98bf-a5bf65af8b8f) is increasing 7
    Bookkeeper (urn:uuid:4f2d4e78-7a33-4c4f-86ac-7c415a7205f4) got 8 back
    Adder (urn:uuid:f50029eb-7cea-4ab9-98bf-a5bf65af8b8f) is increasing 8
    Bookkeeper (urn:uuid:4f2d4e78-7a33-4c4f-86ac-7c415a7205f4) got 9 back
    Adder (urn:uuid:f50029eb-7cea-4ab9-98bf-a5bf65af8b8f) is increasing 9
    Bookkeeper (urn:uuid:4f2d4e78-7a33-4c4f-86ac-7c415a7205f4) got 10 back


Pool of actors sharing work
===========================

.. literalinclude:: ../examples/resolver.py
