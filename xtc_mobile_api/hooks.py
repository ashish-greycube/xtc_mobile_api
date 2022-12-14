from . import __version__ as app_version

app_name = "xtc_mobile_api"
app_title = "XTC API"
app_publisher = "GreyCube Technologies"
app_description = "API to create picklist from mobile"
app_icon = "octicon octicon-file-directory"
app_color = "red"
app_email = "admin@greycube.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/xtc_mobile_api/css/xtc_mobile_api.css"
# app_include_js = "/assets/xtc_mobile_api/js/xtc_mobile_api.js"

# include js, css files in header of web template
# web_include_css = "/assets/xtc_mobile_api/css/xtc_mobile_api.css"
# web_include_js = "/assets/xtc_mobile_api/js/xtc_mobile_api.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "xtc_mobile_api/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Batch" : "public/js/batch.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "xtc_mobile_api.install.before_install"
# after_install = "xtc_mobile_api.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "xtc_mobile_api.uninstall.before_uninstall"
# after_uninstall = "xtc_mobile_api.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "xtc_mobile_api.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",	
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Quality Inspection": {
		"on_update": "xtc_mobile_api.api.on_save_submit_quality_inspection"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"xtc_mobile_api.tasks.all"
#	],
#	"daily": [
#		"xtc_mobile_api.tasks.daily"
#	],
#	"hourly": [
#		"xtc_mobile_api.tasks.hourly"
#	],
#	"weekly": [
#		"xtc_mobile_api.tasks.weekly"
#	]
#	"monthly": [
#		"xtc_mobile_api.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "xtc_mobile_api.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "xtc_mobile_api.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "xtc_mobile_api.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"xtc_mobile_api.auth.validate"
# ]

