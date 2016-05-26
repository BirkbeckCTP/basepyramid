from pyramid.config import Configurator


import assets

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.registry.settings.setdefault('webassets.bundles', 'basepyramid:assets.yaml')
    config.include(assets)
    config.commit()

    config.add_route('base.html', '/')
    config.scan(__name__)
    config.scan('.views')
    return config.make_wsgi_app()
