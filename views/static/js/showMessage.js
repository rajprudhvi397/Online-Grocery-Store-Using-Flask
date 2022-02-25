function showMessage(messageType,message){
    if (messageType == 'success'){
        let successMessageBox = document.getElementsByClassName('succes-popup-message')[0];
        document.getElementById('success-text').innerText = message
        successMessageBox.classList.remove('hide-message');
        setTimeout(() => {
            successMessageBox.classList.add('hide-message');
        }, 200);
    }

    else if (messageType == 'warning'){
        let successMessageBox = document.getElementsByClassName('warning-popup-message')[0];
        document.getElementById('warning-text').innerText = message
        successMessageBox.classList.remove('hide-message');
        setTimeout(() => {
            successMessageBox.classList.add('hide-message');
        }, 2000);
    }
}