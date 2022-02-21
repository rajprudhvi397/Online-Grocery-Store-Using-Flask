let closeIcon = document.getElementsByClassName('close-message-img')[0];
let messageDiv = document.getElementsByClassName('message')[0];

closeIcon.addEventListener('click',()=>{
    messageDiv.style.display = 'none';
})


// The following code will open and close modal when clicked on specific kind of elements

// document.getElementById('success-call').addEventListener('click',()=>{
//     let successMessageBox = document.getElementsByClassName('success-popup-message')[0];
//         document.getElementById('success-text').innerText = 'Success1'
//         successMessageBox.classList.remove('hide-message');
//         setTimeout(() => {
//             successMessageBox.classList.add('hide-message');
//         }, 2000);
// });

// document.getElementById('warning-call').addEventListener('click',()=>{
//     let successMessageBox = document.getElementsByClassName('warning-popup-message')[0];
//         document.getElementById('warning-text').innerText = 'Warning1'
//         successMessageBox.classList.remove('hide-message');
//         setTimeout(() => {
//             successMessageBox.classList.add('hide-message');
//         }, 2000);
// });