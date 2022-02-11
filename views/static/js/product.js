let minusButton = document.getElementById('minus-button');
let plusButton = document.getElementById('plus-button');
let quantityCountSection = document.getElementById('quantityCountSection');

minusButton.addEventListener('click',()=>{
    if (quantityCountSection.innerText != 1) {
        quantityCountSection.innerText = parseInt(quantityCountSection.innerText) - 1
    }
});

plusButton.addEventListener('click',()=>{
    quantityCountSection.innerText = parseInt(quantityCountSection.innerText) + 1
});
