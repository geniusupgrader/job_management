from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Job Management"),
			"items": [
				{
					"type": "doctype",
					"name": "job_application_job_management",
					"label": _("Job Application"),
					"description": _("Job Application"),
				},
				{
					"type": "doctype",
					"name": "application_method_job_management",
					"label": _("Application Method"),
					"description": _("Application Method"),
				},
				{
					"type": "doctype",
					"name": "Job_Classification_job_management",
					"label": _("Job Classification"),
					"description": _("Job Classification"),
				},
				{
					"type": "doctype",
					"name": "Cover_Letter_job_management",
					"label": _("Cover Letter"),
					"description": _("Text Template"),
				},
				{
					"type": "doctype",
					"name": "Cover_Letter_job_management",
					"label": _("Cover Letter"),
					"description": _("Text Template"),
				}
			]
		}
	]