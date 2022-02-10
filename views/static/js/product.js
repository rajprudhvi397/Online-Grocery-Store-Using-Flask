let minusButton = document.getElementsByClassName('minus-section')[0];
let plusButton = document.getElementsByClassName('plus-section')[0];
let quantityCountSection = document.getElementsByClassName('quantity-count')[0];
let quantityValue = parseInt(quantityCountSection.innerHTML);

minusButton.addEventListener('click',()=>{
    console.log(quantityValue);
    quantityCountSection.textContent = quantityValue - 1;
});

plusButton.addEventListener('click',()=>{
    console.log(quantityValue);
    quantityCountSection.textContent = quantityValue + 1;
});