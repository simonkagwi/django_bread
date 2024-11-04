from .base import BreadTestCase


class BreadTemplateResolutionTest(BreadTestCase):
    def setUp(self):
        super().setUp()
        # skip 'add' since it uses 'edit' template
        self.bread_names = ["browse", "read", "edit", "delete"]
        self.app_name = self.model._meta.app_label

    def test_default_template_resolution(self):
        for bread_name in self.bread_names:
            vanilla_template_name = "{}/{}_{}.html".format(
                self.app_name,
                self.model_name,
                bread_name,
            )
            default_bread_template_name = f"bread/{bread_name}.html"
            expected_templates = [
                vanilla_template_name,
                default_bread_template_name,
            ]
            get_method_name = f"{bread_name}_view"
            view_class = getattr(self.bread, get_method_name)
            view = view_class(bread=self.bread, model=self.bread.model)
            self.assertEqual(view.get_template_names(), expected_templates)

    def test_customized_template_resolution(self):
        self.bread.template_name_pattern = "mysite/bread/{view}.html"

        for bread_name in self.bread_names:
            vanilla_template_name = "{}/{}_{}.html".format(
                self.app_name,
                self.model_name,
                bread_name,
            )
            custom_template_name = f"mysite/bread/{bread_name}.html"
            default_bread_template_name = f"bread/{bread_name}.html"
            expected_templates = [
                vanilla_template_name,
                custom_template_name,
                default_bread_template_name,
            ]
            get_method_name = f"{bread_name}_view"
            view_class = getattr(self.bread, get_method_name)
            view = view_class(bread=self.bread, model=self.bread.model)
            self.assertEqual(view.get_template_names(), expected_templates)
