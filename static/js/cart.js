var total = []
function countFunction(price,amo){

    total += price
    console.log(total)


}

function cerealFuntion(cerealId, price) {
    var cerealId = cerealId
    var price = price
    var url = '/homepage/cereal/update_item'
    console.log(url)

    fetch(url, {
        credentials: 'include',
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'cerealId': cerealId, 'price':price})
    })

}

function toyfunction(toyid, price) {
    var toyId = toyid
    var price = price

    var url = '/homepage/cereal/update_item'

    fetch(url, {
        credentials: 'include',
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'toyId': toyId, 'price':price})
    })
}

function removeCerealFromCart(id, amount) {
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

function removeToyFromCart(id, amount) {
    fetch("", {
        credentials: "include",
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'toyid': id,
            'amount': amount
        })
    }).then((response) => {
        return response.json()
    })
}
