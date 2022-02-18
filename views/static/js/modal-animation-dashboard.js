let deleteCategoryBtn = document.getElementsByClassName('delete-category-btn');
let deleteCheckModal = document.getElementsByClassName('delete-check-modal')[0]
let modalCancelBtn = document.getElementsByClassName('cancel-btn')[0];

Array.from(deleteCategoryBtn).forEach((element)=>{
    element.addEventListener('click',()=>{
        deleteCheckModal.classList.remove('hide-modal');
        deleteCheckModal.classList.add('dim-background');
    })
});

modalCancelBtn.addEventListener('click',()=>{
    deleteCheckModal.classList.add('hide-modal');
    deleteCheckModal.classList.remove('dim-background');
});