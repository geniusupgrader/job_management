from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Job Seeking"),
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