from django.template import Context, Template


def test_plausible_renders_with_data_domain_from_request(rf):
    request = rf.get("/", SERVER_NAME="example.com")
    template = Template("{% load plausible %}{% plausible %}")
    context = Context({"request": request})
    assert (
        template.render(context)
        == '<script data-domain="example.com" src="/js/script.js" defer></script>'
    )


def test_plausible_uses_plausible_domain_if_defined(rf, settings):
    settings.PLAUSIBLE_DOMAIN = "example2.com"
    request = rf.get("/", SERVER_NAME="example.com")
    template = Template("{% load plausible %}{% plausible %}")
    context = Context({"request": request})
    assert (
        template.render(context)
        == '<script data-domain="example2.com" src="/js/script.js" defer></script>'
    )