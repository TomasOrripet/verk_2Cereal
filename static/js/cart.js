var updateBtn = document.getElementsByClassName('update-cart')

for ( i = 0; i < updateBtn.length; i++) {
    updateBtn[i].addEventListener('click', function (){
        var cerealId = this.dataset.cereal
        var action = this.dataset.action
        console.log('cerealId:',cerealId, 'action:' , action)
    })
}