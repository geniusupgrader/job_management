from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Job Seeker"),
			"items": [
				{
					"type": "doctype",
					"name": "Own Application",
					"description":_("Own Application"),
					"onboard": 1,
				}
			]
		}
	]