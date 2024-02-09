
var expiredPoIds = [];

frappe.ui.form.on('Purchase Receipt', {
    onload: function(frm) {
        fetchAndStoreExpiredPurchaseOrders();
    }
});

function fetchAndStoreExpiredPurchaseOrders() {
    frappe.call({
        method: 'purchase_validation.api.get_all_purchase_orders',
        callback: function(response) {
            var purchaseOrders = response.message;
            checkExpiredPurchaseOrders(purchaseOrders);
        }
    });
}

function checkExpiredPurchaseOrders(purchaseOrders) {
    if (purchaseOrders && purchaseOrders.length > 0) {
        expiredPoIds = [];
        purchaseOrders.forEach(function(po) {
            var expireDate = po.expire_date ? new Date(po.expire_date) : null;
            if (expireDate && expireDate < new Date()) {
                expiredPoIds.push(po.name);
            }
        });
    }
}

frappe.ui.form.on('Purchase Receipt', {
    onload: function(frm) {
       
        setInterval(function() {
            checkExpiredPurchaseOrderItems();
        }, 1000);
    }
});

function checkExpiredPurchaseOrderItems() {
    var items_table = cur_frm.fields_dict['items'].grid;
    var items_data = items_table.get_data();

    items_data.forEach(function(item) {
        var po_id = item.purchase_order || '';
        if (expiredPoIds.includes(po_id)) {
          
            item.item_code = '';
            item.item_name = '';
            item.qty = '';
            item.rate = '';
            item.amount = ''; 
        }
    });


    items_table.refresh();
}




frappe.ui.form.on('Purchase Receipt', {
    onload: function(frm) {
       
        setInterval(function() {
            copyQtyToPOQty();
        }, 1000);
    }
});

function copyQtyToPOQty() {
    var items = cur_frm.doc.items || [];
    items.forEach(function(item) {
     
    
            item.po_qty = item.qty;
    
    });

   
    cur_frm.refresh_field('items');
}





frappe.ui.form.on('Purchase Receipt', {
    onload: function(frm) {
        frm.fields_dict.expire_date.$input.on('focusout', function() {
            var expireDate = frm.fields_dict.expire_date.get_value();
            var today = frappe.datetime.get_today();
            var expireDateObj = new Date(expireDate);
            var todayObj = new Date(today);
            if (expireDateObj < todayObj) {
                var fieldsToClear = ['total_qty','total'];

                fieldsToClear.forEach(function(field) {
                    frm.set_value(field, '');
                });
         
                frappe.msgprint('<span style="color:red;">Warning: Creating a Purchase Receipt against an expired Purchase Order is not allowed.</span>');
            }
        });
    }
});












































































































































































