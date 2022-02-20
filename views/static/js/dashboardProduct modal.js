let editProductDetailsBtn = document.getElementsByClassName('edit-product-details-btn');

Array.from(editProductDetailsBtn).forEach((element)=>{
    let modal = document.getElementById(element.classList[2]);    
    element.addEventListener('click',(ev)=>{
        modal.classList.add('dim-background');
        modal.classList.remove('make-invisible');
    })
})