let openModalBtn = document.getElementsByClassName('open-form-modal-button')[0];
let formModal = document.getElementsByClassName('form-modal')[0];
let closeModalIcon = document.getElementsByClassName('close-modal-icon')[0];
let modalIsVisible = false;

openModalBtn.addEventListener('click',()=>{
    console.log('reached');
    formModal.classList.remove('hide-modal');
    formModal.classList.add('dim-background');
    modalIsVisible = true;
});

closeModalIcon.addEventListener('click',()=>{
    formModal.classList.add('hide-modal');
    formModal.classList.remove('dim-background');
})