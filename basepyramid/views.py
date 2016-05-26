'''
Copyright (c) 2013-2014 Hypothes.is Project and contributors

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''


from pyramid.view import view_config
from pyramid.view import view_defaults


from jinja2 import Environment, PackageLoader

jinja_env = Environment(loader=PackageLoader(__package__, 'templates'))

@view_config(route_name='base.html')
def home(request):
    return _render_app(request)

def asset_urls(webassets_env, name):
    return webassets_env[name].urls()

def _render_app(request):
    request.response.text = render_app_html(webassets_env=request.webassets_env)
    return request.response

def render_app_html(webassets_env):
     template = jinja_env.get_template('base.html.jinja2')
     assets_dict = _app_html_context(webassets_env=webassets_env)
     return template.render(assets_dict)

def _app_html_context(webassets_env):
    return {
        'app_js_urls': asset_urls(webassets_env, 'app_js')
    }

