app_name = "purchase_validation"
app_title = "Purchase Validation"
app_publisher = "adnan"
app_description = "we use it to validate some fields"
app_email = "adnanjohan54@gmail.com"
app_license = "mit"

# hooks.py

fixtures = ["Custom Field"]


# app_include_js = ["/assets/purchase_validation/js/expiry_validation.js"]

# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/purchase_validation/css/purchase_validation.css"
# app_include_js = "/assets/purchase_validation/js/purchase_validation.js"

# include js, css files in header of web template
# web_include_css = "/assets/purchase_validation/css/purchase_validation.css"
# web_include_js = "/assets/purchase_validation/js/purchase_validation.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "purchase_validation/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}


doctype_js = {
    'Purchase Receipt': 'public/js/expiry_validation.js',
    'Purchase Invoice': 'public/js/expiry_validation.js',
    'Purchase Receipt Item': 'public/js/expiry_validation.js',
    'Purchase Invoice': 'public/js/expire_validation_pi.js',

}


# Scheduler


# Scheduler


# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "purchase_validation/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "purchase_validation.utils.jinja_methods",
# 	"filters": "purchase_validation.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "purchase_validation.install.before_install"
# after_install = "purchase_validation.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "purchase_validation.uninstall.before_uninstall"
# after_uninstall = "purchase_validation.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "purchase_validation.utils.before_app_install"
# after_app_install = "purchase_validation.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "purchase_validation.utils.before_app_uninstall"
# after_app_uninstall = "purchase_validation.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "purchase_validation.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }
# override_doctype_controller = {
#     "Purchase Order": "purchase_validation.purchase_validation.doctype.purchase_order.purchase_order.override_purchase_order_controller"
# }
# purchase_validation/hooks.py


# List all hooks that you want to override here
# purchase_validation/hooks.py

# List all hooks that you want to override here



# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"purchase_validation.tasks.all"
# 	],
# 	"daily": [
# 		"purchase_validation.tasks.daily"
# 	],
# 	"hourly": [
# 		"purchase_validation.tasks.hourly"
# 	],
# 	"weekly": [
# 		"purchase_validation.tasks.weekly"
# 	],
# 	"monthly": [
# 		"purchase_validation.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "purchase_validation.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "purchase_validation.event.get_events"
# }
# custom_app/hooks.py

# purchase_validation/hooks.py

# List all hooks that you want to override here
# override_whitelisted_methods = {
#     "erpnext.buying.doctype.purchase_order.purchase_order.validate": "purchase_validation.overrides.override_methods"
# }


#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "purchase_validation.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["purchase_validation.utils.before_request"]
# after_request = ["purchase_validation.utils.after_request"]

# Job Events
# ----------
# before_job = ["purchase_validation.utils.before_job"]
# after_job = ["purchase_validation.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"purchase_validation.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }



# from frappe import _

# def customize_form(doc, handler=""):
#     if doc.name == "Purchase Order":
#         doc.fields.append({
#             "label": _("Expire Date"),
#             "fieldname": "expire_date",
#             "fieldtype": "Date"
#         })



# doc_events = {
#     "*": {
#         "on_update": "purchase_validation.purchase_validation.hooks.customize_form"
#     }
# }











import frappe

def get_hooks():
    return {
        'whitelist_methods': {
            'purchase_validation.api.fetch_items_from_po_in_pr': True
        }
    }


