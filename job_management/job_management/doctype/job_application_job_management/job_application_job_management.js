// Copyright (c) 2020, Robin Rosenstock and contributors
// For license information, please see license.txt

frappe.ui.form.on('Job_application_job_management', {
	address: function(frm) {
		frappe.db.get_doc('Address', cur_frm.doc.address).then(doc =>{ 
			var address_line_1 = doc.address_line1;
			var postal_code = doc.pincode;
			var city = doc.city;
			frm.set_value('address_read_only', address_line_1+", "+postal_code+" "+city)
			frm.refresh_field('address_read_only');
		})
	}
});

frappe.ui.form.on('Job_application_job_management', {
	contact_person: function(frm) {
		frappe.db.get_doc('Contact', cur_frm.doc.contact_person).then(doc =>{ 
			var first_name = doc.first_name;
			var last_name = doc.last_name;
			frm.set_value('contact_read_only', first_name+" "+last_name)
			frm.refresh_field('contact_read_only');
		})
	}
});