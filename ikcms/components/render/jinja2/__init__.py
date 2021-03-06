import jinja2

from ..base import RenderComponent


class Jinja2Component(RenderComponent):

    filters = {}
    globals = {}
    extensions = []
    autoescape = True
    paths = []

    def __init__(self, app):
        super().__init__(app)
        self.paths = [path.format(**app.cfg.as_dict()) for path in self.paths]
        self._env = self._make_env()

    def _make_env(self):
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(self.paths),
            autoescape=self.autoescape,
            extensions=self.extensions)
        env.filters.update(self.filters)
        env.globals.update(self.globals)
        return env

    def render(self, template_name, context=None):
        context = context or {}
        return self._env.get_template(template_name).render(**context)
    __call__ = render


component = Jinja2Component.create_cls
