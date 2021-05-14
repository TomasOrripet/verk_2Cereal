function cerealFuntion() {
    var updateBtn = document.getElementsByClassName('update-cart')
    for (i = 0; i < updateBtn.length; i++) {
        console.log("button press")
        updateBtn[i].addEventListener('click', function () {
            var cerealName = this.dataset.cerealname
            var cerealId = this.dataset.cerealid
            var price = this.dataset.price
            var action = this.dataset.action
            console.log('cerealName:', cerealName, 'cerealId:', cerealId, 'action:', action)

            console.log('User:', user)
            if (user == 'AnonymousUser') {
                console.log('User is anonymous')
            } else {
                updateUserOrder(cerealName, cerealId, price, action)
            }
        })
    }

    function updateUserOrder(cerealName, cerealId, price, action) {
        console.log('User is authenticated, sending data....')

        var url = '/homepage/cereal/update_item'
        console.log(url)

        fetch(url, {
            credentials: 'include',
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({'cerealName': cerealName, 'cerealId': cerealId, 'price': price, 'action': action})
        })
            .then((response) => {
                return response.json()
            })
            .then((data) => {
                console.log('data:', data)
            })
    }
}
function toyfunction () {
    var toyUpdateBtn = document.getElementsByClassName('update-toy')
    for (i = 0; i < toyUpdateBtn.length; i++) {
        console.log("button press")
        toyUpdateBtn[i].addEventListener('click', function () {
            var toyId = this.dataset.toyid

            console.log('toyId:', toyId)

            console.log('User:', user)
            if (user == 'AnonymousUser') {
                console.log('User is anonymous')
            } else {
                updateUserOrder(toyId)
            }
        })
    }

    function updateUserOrder(toyId) {
        console.log('User is authenticated, sending data....')

        var url = '/homepage/cereal/update_item'
        console.log(url)

        fetch(url, {
            credentials: 'include',
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({'toyId': toyId})
        })
            .then((response) => {
                return response.json()
            })
            .then((data) => {
                console.log('data:', data)
            })
    }
}

function removeFromCart(id, amount){
    var url = 'homepage/cart/removeitem'
    console.log(amount)
    console.log(id)
    var removefromcart = document.getElementsByClassName('remove-from-cart')
    fetch("", {
        credentials: "include",
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'cerealid': id,
            'amount': amount
        })
            }).then((response) => {
                return response.json()
            })
}