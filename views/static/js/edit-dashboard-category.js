// This function will send a post request to the specified through which we will edit a category in database
async function editCategory(data){

    addCSSLoader(); // Adding CSS Loader

    try{

        let response = await fetch(`${window.origin}/dashboard/dashboardCategory/editDashboardCategory/`,{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (response.status == 200){

            try {
                let responseJson = await response.json(); // Waiting for JSON response
                removeCSSLoader() // Removing CSS Loader
                showAlert('The Category has been edited','success');

            } catch (error) {
                removeCSSLoader() // Removing CSS Loader
                showAlert('Some Error Occured while editing the category','error');
            }
        }
        else{
            removeCSSLoader() // Removing CSS Loader
            showAlert('Some Error Occured while editing the category','error');
        }

    }
    catch(error){
        removeCSSLoader() // Removing CSS Loader
        showAlert('Some Error Occured while editing the category 3','error');
    }
}

// The following function will popup an alert for specific categories
function showAlert(message,category){
    if (category == 'success'){
        let successMessageBox = document.getElementsByClassName('success-popup-message')[0];
        document.getElementById('success-text').innerText = message
        successMessageBox.classList.remove('hide-message');
        setTimeout(() => {
            successMessageBox.classList.add('hide-message');
        }, 2000);
    }

    else if (category == 'error'){
        let successMessageBox = document.getElementsByClassName('warning-popup-message')[0];
        document.getElementById('warning-text').innerText = message
        successMessageBox.classList.remove('hide-message');
        setTimeout(() => {
            successMessageBox.classList.add('hide-message');
        }, 2000);
    }
}

// This function will add a CSS Loader
function addCSSLoader(){
    // Adding CSS Loader
    loader.classList.add('loader-active');
    loader.classList.remove('hide-loader');
    document.body.style.overflowY = 'hidden'; // Removes scrollbar
}

// This function will remove a CSS Loader
function removeCSSLoader(){
    loader.classList.remove('loader-active');
    loader.classList.add('hide-loader');
    document.body.style.overflowY = 'initial'; // Adding scrollbar
}

Array.from(document.getElementsByClassName('update-name-btn')).forEach((element)=>{
    element.addEventListener('click',(ev)=>{
        let categoryId = ev.target.classList[0] // Getting the category id from class
        let categoryNameInput = document.getElementById(`${categoryId}-input`);
        if (categoryNameInput.value == ''){
            return;
        }
    
        let data = {
            'new-category-name': categoryNameInput.value,
            'categoryId': categoryId
        }; // Creating a object to send it as request
    
        editCategory(data); // Running function to send fetch calls
        
    });
});