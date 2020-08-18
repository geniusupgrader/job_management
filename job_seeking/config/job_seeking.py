from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Job Seeking"),
			"items": [
				{
					"type": "doctype",
					"name": "job_application_job_seeking",
					"description":_("Job Application"),
					"onboard": 1,
				}
			]
		}
	]