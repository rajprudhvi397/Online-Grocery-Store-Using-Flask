// This function will send a post request to the specified through which we will delete a category in database

// let loader = document.getElementsByClassName('loader-div')[0] // Getting the loader

async function deleteCategory(data){

    addCSSLoader(); // Adding CSS Loader

    try{

        let response = await fetch(`${window.origin}/dashboard/dashboardCategory/removeDashboardCategory/`,{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (response.status == 200){

            try {
                let responseJson = await response.json(); // Waiting for JSON response
                hideModal() // Hiding Modal
                removeCategoryDiv(data['category-Id']) // Removing div from parent directory
                removeCSSLoader() // Removing CSS Loader
                showAlert('The Category has been deleting','success');

            } catch (error) {
                hideModal() // Hiding Modal
                removeCSSLoader() // Removing CSS Loader
                showAlert('Some Error Occured while deleting the category','error');
            }
        }
        else{
            hideModal() // Hiding Modal
            removeCSSLoader() // Removing CSS Loader
            showAlert('Some Error Occured while deleting the category','error');
        }

    }
    catch(error){
        hideModal() // Hiding Modal
        removeCSSLoader() // Removing CSS Loader
        showAlert('Some Error Occured while deleting the category ','error');
    }
}

// This function will hide the delete modal
function hideModal() {
    let deleteCheckModal = document.getElementsByClassName('delete-check-modal')[0]
    deleteCheckModal.classList.add('hide-modal');
    deleteCheckModal.classList.remove('dim-background');
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
    };
};

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

Array.from(document.getElementsByClassName('delete-category-btn')).forEach((element)=>{
    element.addEventListener('click',(ev)=>{
        let categoryId = ev.target.classList[0] // Getting the category id from class
        document.querySelector('.delete-btn').id = `${categoryId}`; // Setting id of button of modal for later use
        
    });
});

document.getElementsByClassName('delete-btn')[0].addEventListener('click',(ev)=>{
    let deleteBtnId = ev.target.id; // Getting id of delete btn
    // let categoryId = deleteBtnId.splice(0,deleteBtnId.length-17); // Getting category id from id of element

    let data = {
        'category-Id': deleteBtnId
    } // Creating an object to send it in a fetch call

    deleteCategory(data); // Running function to make fetch calls
});

function removeCategoryDiv(categoryId){
    let categoryDiv = document.getElementById(`${categoryId}-input`).parentElement; // Getting the category div
    categoryDiv.style.display = 'none'; // Doing display none to remove element from parent directory
}