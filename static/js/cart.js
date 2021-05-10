var updateBtn = document.getElementsByClassName('update-cart')

console.log("yaaa   ass",updateBtn )
for ( i = 0; i < updateBtn.length; i++) {
    console.log("button press")
    updateBtn[i].addEventListener('click', function (){
        var cerealId = this.dataset.cereal
        var action = this.dataset.action
        console.log('cerealId:',cerealId, 'action:' , action, "asshole")
    })
}