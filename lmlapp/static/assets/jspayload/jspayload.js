 $(document).ready(function () {
    let loc = window.location.origin + "/registrationpaydetails/"
    $.get(loc, function(data, status){
       console.log(data, status);

       loadPayp(data);
    });


})
var total = 0;
let user_id;
let reg_no;
let user_name;
 function loadPayp(d) {
   total =  d.reg_amount;
   user_id = d.user_id;
   user_name = d.user_name;
   reg_no = d.reg_no;
    paypal.Buttons({
        style: {
            color:  'gold',
            shape:  'pill',
            label:  'pay',
            height: 40
        },
        // Set up the transaction
        createOrder: function(data, actions) {
            return actions.order.create({
                purchase_units: [{
                    amount: {
                        value: total
                    }
                }]
            });
        },

        // Finalize the transaction
        onApprove: function(data, actions) {
            return actions.order.capture().then(function(details) {
                // Show a success message to the buyer
                console.log(details)
                alert('Transaction completed by ' + details.payer.name.given_name + '!');
            });
        }
    }).render('#paypal-button-container')
 }