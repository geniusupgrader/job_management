from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Job Management"),
			"items": [
				{
					"type": "doctype",
					"name": "Job_application_job_management",
					"label": _("Job Application"),
					"description": _("Job Application"),
				},
				{
					"type": "doctype",
					"name": "Application_method_job_management",
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
					"name": "Curriculum_vitae_job_management",
					"label": _("Curriculum Vitae (CV)"),
					"description": _("Text Template"),
				}
			]
		}
	]