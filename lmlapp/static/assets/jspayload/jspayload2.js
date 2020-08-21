 $(document).ready(function () {
    let loc = window.location.origin + "/companyregistrationpaydetails/"
    $.get(loc, function(data, status){
       // console.log(data, status);
       loadPayp(data);
    });
})
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function loadPayp(d) {
   var total =  d.reg_amount;
   var currency = d.currency;
   var ammount = total/currency;

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
                        value: ammount.toFixed(2),
                    }
                }]
            });
        },

        // Finalize the transaction
        onApprove: function(data, actions) {
            return actions.order.capture().then(function(details) {

                completePayment(details)
                // alert('Transaction completed by ' + details.payer.name.given_name + '!');
            });
        }
    }).render('#paypal-button-container')
 }

 function completePayment(data){
    var url = window.location.origin+"/company_payment_complete/";
    $.ajax({
        processData: false,
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        type: 'POST',
        url: url,
        data: JSON.stringify(data),
        dataType: 'json',
        success: function(data){
            console.log(data)
            if (data['status'] === 'success' && data['payment'] === 'done' ){
                window.location = window.location.origin+'/company_payment-done/';
            }
            else if(data['status'] === 'error' && data['payment'] === 'reversed' ){
                window.location = window.location.origin+'/company_payment-cancelled/';
            }
        },
        error: function(){

        },

    });
 }
