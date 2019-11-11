from django.shortcuts import render
from django.views import generic
from .models import Message
from django.forms.models import model_to_dict

class ReactMixin(object):
	template_name = 'base.html'

	def get_context_data(self, *args, **kwargs):
		context = super(ReactMixin, self).get_context_data(*args, **kwargs)
		context["react_props"] = self.get_react_props(context)
		context["page_name"] = self.get_page_name()
		context["title"] = self.get_title()
		return context

	def get_react_props(self, context):
		raise NotImplementedError()

	def get_page_name(self, context):
		raise NotImplementedError()

	def get_title(self):
		raise NotImplementedError()


class IndexView(ReactMixin, generic.ListView):
	queryset = Message

	def get_react_props(self, context):
		return {"messages": list(self.queryset.objects.values())}

	def get_page_name(self):
		return "main"

	def get_title(self):
		return "Messages List -- Webpack Django Test"


class MessageDetailView(ReactMixin, generic.DetailView):
	model = Message

	def get_react_props(self, context):
		return {"message": model_to_dict(self.object)}

	def get_page_name(self):
		return "message"

	def get_title(self):
		return "Single Message -- Webpack Django Test"