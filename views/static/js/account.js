let editProfileBtn = document.getElementsByClassName('edit-profile-button')[0];
let editProfileModal = document.getElementsByClassName('edit-profile-modal')[0];
let modalIsVisible = false;

editProfileBtn.addEventListener('click',()=>{
    editProfileModal.classList.remove('hide-modal');
    editProfileModal.classList.add('dim-background');
    modalIsVisible = true;
});