
import frappe
@frappe.whitelist()
def get_all_purchase_orders():
    try:
        purchase_orders = frappe.get_all("Purchase Order",
            fields=["name", "supplier", "expire_date"],
            filters={"docstatus": 1})
        
        for po in purchase_orders:
            po['items'] = frappe.get_all("Purchase Order Item",
                fields=["item_code", "qty", "rate"],
                filters={"parent": po['name']})
        
        return purchase_orders
    except Exception as e:
        frappe.throw(f"Error fetching Purchase Orders: {str(e)}")



@frappe.whitelist()
def get_purchase_receipt_data():
    purchase_receipts = frappe.get_list('Purchase Receipt', fields=['name', 'items','expire_date'], filters={})
    processed_data = []

    for pr in purchase_receipts:
        pr_doc = frappe.get_doc('Purchase Receipt', pr.name)
        pr_data = {
            'name': pr.name,
            'items': pr_doc.items,
            'expire_date': pr.expire_date
        }
        processed_data.append(pr_data)

    return processed_data














