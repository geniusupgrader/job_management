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
					"label": _("Job Application"),
					"description": _("Job Application"),
				},
				{
					"type": "doctype",
					"name": "application_method_job_seeking",
					"label": _("Application Method"),
					"description": _("Application Method"),
				},
				{
					"type": "doctype",
					"name": "Job_Classification_job_seeking",
					"label": _("Job Classification"),
					"description": _("Job Classification"),
				},
				{
					"type": "doctype",
					"name": "Text_Template_job_seeking",
					"label": _("Text Template"),
					"description": _("Text Template"),
				}
			]
		}
	]