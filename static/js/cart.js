var updateBtn = document.getElementsByClassName('update-cart')
for ( i = 0; i < updateBtn.length; i++) {
    console.log("button press")
    updateBtn[i].addEventListener('click', function(){
        var cerealName = this.dataset.cerealname
        var cerealId = this.dataset.cerealid
        var cerealprice = this.dataset.price
        var action = this.dataset.action
        console.log('cerealName:',cerealName,'cerealId:',cerealId, 'action:' , action)

        console.log('User:',user)
        if ( user == 'AnonymousUser'){
            console.log('User is anonymous')
        }else{
            updateUserOrder(cerealName,cerealId,cerealprice,action)
        }
    })
}
function updateUserOrder(cerealName,cerealId,cerealprice ,action){
    console.log('User is authenticated, sending data....')

    var url = '/homepage/cereal/update_item'
    console.log(url)

    fetch(url, {
        credentials: 'include',
        method:'POST',
        headers:{
            'X-CSRFToken':csrftoken,
            'Content-Type':'application/json'
        },
        body:JSON.stringify({'cerealName':cerealName,'cerealId': cerealId,'cerealprice': cerealprice, 'action': action})
    })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log('data:',data)
        })
}