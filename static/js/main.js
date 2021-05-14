var UpdateBtn = document.getElementsByClassName('update-toy')
flag = true;
setTimeout(function(){ flag = false; }, 10000000);
for (i = 0; i < UpdateBtn.length; i++) {
    console.log("button press")
    UpdateBtn[i].addEventListener('click', function () {
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
