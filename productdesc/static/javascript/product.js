document.addEventListener("DOMContentLoaded", function () {
    // Get elements by their ID
    const decreaseBtn = document.getElementById("btnminus");
    const increaseBtn = document.getElementById("btnplus");
    const quantityInput = document.getElementById("btntext");
    const pid = document.getElementById("pid");
    const btncart = document.getElementById("btncart");
    const statuspara = document.getElementById("statuspara")
    

        decreaseBtn.addEventListener("click", function () {
            let currentValue = parseInt(quantityInput.value);
            if (currentValue > 1) {
                quantityInput.value = currentValue - 1;
            }
        });

        increaseBtn.addEventListener("click", function () {
            let currentValue = parseInt(quantityInput.value);
            let maxValue = parseInt(quantityInput.getAttribute("max"));
            if (currentValue < maxValue) {
                quantityInput.value = currentValue + 1;
            }
        });

        btncart.addEventListener("click", function () {
            let currentValue = parseInt(quantityInput.value);
            if (currentValue > 0){

                let postobj = {
                    productquantity: currentValue,
                    pid:pid.value,
                }
                fetch("/addtocart",{
                    method: 'POST',
                    credentials: 'same-origin',
                    headers: {
                        'Accept': 'application/json',
                        'X-Requested-With': 'XMLHttpRequest',
                        'X-CSRFToken': document.querySelector('[name="csrfmiddlewaretoken"]').value
                    },
                    body: JSON.stringify(postobj)
                })
                .then(response => {
                    return response.json();
                }) 
                .then(data => {
                    alert(data['status'])
                });
            }else{
                alert("please enter quantity")
            }
        });
    });






    
