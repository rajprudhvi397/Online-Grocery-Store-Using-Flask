function showMessage(messageType,message){
    if (messageType == 'success'){
        let successMessageBox = document.getElementsByClassName('succes-popup-message')[0];
        // successMessageBox.firstChild.textContent = message;
        successMessageBox.classList.remove('hide-message');
        setTimeout(() => {
            successMessageBox.classList.add('hide-message');
        }, 200);
    }

    if (messageType == 'warning'){
        let successMessageBox = document.getElementsByClassName('warning-popup-message')[0];
        successMessageBox.firstChild.textContent = message;
        successMessageBox.classList.remove('hide-message');
        setTimeout(() => {
            successMessageBox.classList.add('hide-message');
        }, 2000);
    }
}

export {showMessage};