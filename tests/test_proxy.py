import pytest

from pykka import ActorDeadError, ActorProxy


class NestedObject(object):
    cat = 'bar.cat'
    pykka_traversable = True


@pytest.fixture(scope='module')
def actor_class(runtime):
    class ActorA(runtime.actor_class):
        bar = NestedObject()

        foo = 'foo'

        def __init__(self):
            super(runtime.actor_class, self).__init__()
            self.cat = 'quox'

        def func(self):
            pass

    return ActorA


@pytest.fixture
def proxy(actor_class):
    proxy = ActorProxy(actor_class.start())
    yield proxy
    try:
        proxy.stop()
    except ActorDeadError:
        pass


def test_repr_is_wrapped_in_lt_and_gt(proxy):
    result = repr(proxy)

    assert result.startswith('<')
    assert result.endswith('>')


def test_repr_reveals_that_this_is_a_proxy(proxy):
    assert 'ActorProxy' in repr(proxy)


def test_repr_contains_actor_class_name(proxy):
    assert 'ActorA' in repr(proxy)


def test_repr_contains_actor_urn(proxy):
    assert proxy.actor_ref.actor_urn in repr(proxy)


def test_repr_contains_attr_path(proxy):
    assert 'bar' in repr(proxy.bar)


def test_str_contains_actor_class_name(proxy):
    assert 'ActorA' in str(proxy)


def test_str_contains_actor_urn(proxy):
    assert proxy.actor_ref.actor_urn in str(proxy)


def test_dir_on_proxy_lists_attributes_of_the_actor(proxy):
    result = dir(proxy)

    assert 'foo' in result
    assert 'cat' in result
    assert 'func' in result


def test_dir_on_proxy_lists_private_attributes_of_the_proxy(proxy):
    result = dir(proxy)

    assert '__class__' in result
    assert '__dict__' in result
    assert '__getattr__' in result
    assert '__setattr__' in result


def test_refs_proxy_method_returns_a_proxy(actor_class):
    proxy_from_ref_proxy = actor_class.start().proxy()

    assert isinstance(proxy_from_ref_proxy, ActorProxy)

    proxy_from_ref_proxy.stop().get()


def test_proxy_constructor_raises_exception_if_actor_is_dead(actor_class):
    actor_ref = actor_class.start()
    actor_ref.stop()

    with pytest.raises(ActorDeadError) as exc_info:
        ActorProxy(actor_ref)

    assert str(exc_info.value) == '{} not found'.format(actor_ref)


def test_actor_ref_may_be_retrieved_from_proxy_if_actor_is_dead(proxy):
    proxy.actor_ref.stop()

    assert not proxy.actor_ref.is_alive()
