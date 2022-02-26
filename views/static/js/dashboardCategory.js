// This function will send a post request to the specified through which we will add a category in database
async function addCategory(data){

    addCSSLoader(); // Adding CSS Loader

    try{

        let response = await fetch(`${window.origin}/dashboard/dashboardCategory/addDashboardCategory/`,{
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
                document.getElementById('add-category-input').value = '';
                showAlert('The Category has been added','success');
                
                return responseJson // To access it from other function

            } catch (error) {
                removeCSSLoader() // Removing CSS Loader
                showAlert('Some Error Occured while creating the category','error');
                return false; // Returning false for function below
            }
        }
        else{
            removeCSSLoader() // Removing CSS Loader
            showAlert('Some Error Occured while creating the category','error');
            return false; // Returning false for function below
        }

    }
    catch(error){
        removeCSSLoader() // Removing CSS Loader
        showAlert('Some Error Occured while creating the category 3','error');
        return false; // Returning false for function below
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

// Setting addEventListener for every click event on add category button
document.getElementById('add-category-btn').addEventListener('click',()=>{
    let categoryNameInput = document.getElementById('add-category-input');
    if (categoryNameInput.value == ''){
        return;
    }

    let data = {
        'category-name': categoryNameInput.value
    } // Creating a object to send it as request

    addCategory(data).then(responseJson =>{
        if (!responseJson){
            return; // Retuning if some error came
        }

        try{
            showCategory(responseJson.categoryName,responseJson.categoryId); // Appending child in parent Element
        }
        catch(error){
            console.log(error);
        }
    })
    
});

// This function will add e
function showCategory(categoryName,categoryId){
    let categoriesParentDiv = document.getElementsByClassName('categories-parent')[0] // Getting the parent div in which all the divs of categories are there
    let isCategoryEmpty = categoriesParentDiv.classList.contains('no-category') ? true : false; // Filling variable with true or false if category table is empty or not

    // what to do if category is empty 
    if (isCategoryEmpty){
        categoriesParentDiv.classList.remove('no-category'); // Removing no-category to make it a non-empty category
        categoriesParentDiv.innerHTML = `
            <div class="category-div">
                <input type="text" name="category-name" placeholder="Enter the Category Name" value="${categoryName}" id="${categoryId}-input" class="category-name-input">
                <a class="${categoryId} update-name-btn">Update Category</a>
                <img src="http://127.0.0.1:5000/static/img/cancel.png" class="${categoryId} delete-category-btn">
            </div>
        `; // Inserting div inside parent directory
        return;
    }

    let categoryDiv = document.createElement('div'); // Creating categoryDiv element
    categoryDiv.className = 'category-div'; // Adding class to the div
    categoryDiv.innerHTML = `
        <div class="category-div">
            <input type="text" name="category-name" placeholder="Enter the Category Name" value="${categoryName}" id="${categoryId}-input" class="category-name-input">
            <a class="${categoryId} update-name-btn">Update Category</a>
            <img src="http://127.0.0.1:5000/static/img/cancel.png" class="${categoryId} delete-category-btn">
        </div>
    `; // Filling content inside div

    categoriesParentDiv.appendChild(categoryDiv); // Inserting element inside parent div
}