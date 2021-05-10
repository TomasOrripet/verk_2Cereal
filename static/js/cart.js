var updateBtn = document.getElementsByClassName('update-cart')
for ( i = 0; i < updateBtn.length; i++) {
    console.log("button press")
    updateBtn[i].addEventListener('click', function(){
        var cerealId = this.dataset.cereal
        var action = this.dataset.action
        console.log('cerealId:',cerealId, 'action:' , action)

        console.log('User:',user)
        if ( user == 'AnonymousUser'){
            console.log('User is anonymous')
        }else{
            updateUserOrder(cerealId,action)
        }
    })
}
function updateUserOrder(cerealId,action){
    console.log('User is authenticated, sending data....')

    var url = 'update_item/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify({'cerealId': cerealId,'action': action})
    })
}