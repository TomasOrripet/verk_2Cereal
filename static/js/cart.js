var total = 0
function countFunction(price){

    total = total + price
    console.log(total)

}

function cerealFuntion(cerealId) {
    var cerealId = cerealId
    var url = '/homepage/cereal/update_item'
    console.log(url)

    fetch(url, {
        credentials: 'include',
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'cerealId': cerealId})
    })

}

function toyfunction(toyid) {
    var toyId = toyid

    var url = '/homepage/cereal/update_item'
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
