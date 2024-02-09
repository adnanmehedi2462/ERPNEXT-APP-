

var expiredReceiptIds = [];

frappe.ui.form.on('Purchase Invoice', {
    onload: function(frm) {
        setInterval(function() {
            checkExpiredPurchaseOrderItems();
        }, 1000);
        fetchAndStoreExpiredPurchaseReceipt();
    }
});

function fetchAndStoreExpiredPurchaseReceipt() {
    frappe.call({
        method: 'purchase_validation.api.get_purchase_receipt_data',
        callback: function(response) {
            var purchaseReceipts = response.message;
            checkExpiredPurchaseReceipts(purchaseReceipts);
        }
    });
}

function checkExpiredPurchaseReceipts(purchaseReceipts) {
    if (purchaseReceipts && purchaseReceipts.length > 0) {
        expiredReceiptIds = [];
        purchaseReceipts.forEach(function(receipt) {
            var expireDate = receipt.expire_date ? new Date(receipt.expire_date) : null;
            if (expireDate && expireDate < new Date()) {
                expiredReceiptIds.push(receipt.name);
            }
        });
    }
}

function checkExpiredPurchaseOrderItems() {
    var items_table = cur_frm.fields_dict['items'].grid;
    var items_data = items_table.get_data();

    items_data.forEach(function(item) {
        var po_id = item.purchase_receipt || '';
        if (expiredReceiptIds.includes(po_id)) {
            
            item.item_code = '';
            item.item_name = '';
            item.qty = '';
            item.rate = '';
            item.amount = ''; 
        }
    });

    
    items_table.refresh();
}

frappe.ui.form.on('Purchase Invoice', {
    refresh: function(frm) {
        var expireDate = frm.doc.expire_date;
        var today = frappe.datetime.get_today();
        var expireDateObj = new Date(expireDate);
        var todayObj = new Date(today);
        
        if (expireDateObj < todayObj) {
            var fieldsToClear = [  'total_qty','total'];

            fieldsToClear.forEach(function(field) {
                frm.set_value(field, '');
            });

            frappe.msgprint('<span style="color:red;">Warning: Creating a Purchase Invoice against an expired Purchase Receipt is not allowed.</span>');
        }
    }
});

