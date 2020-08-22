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
					"name": "Cover_Letter_job_seeking",
					"label": _("Cover Letter"),
					"description": _("Text Template"),
				},
				{
					"type": "doctype",
					"name": "testing_routes",
					"label": _("testing routes"),
					"description": _("testing routes"),
				}
			]
		}
	]