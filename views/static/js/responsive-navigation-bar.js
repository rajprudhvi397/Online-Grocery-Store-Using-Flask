let visibilityELement = document.getElementsByClassName('visibility-resp');
let navigationBar = document.getElementsByClassName('navigation-bar')[0];
let hamburger = document.getElementsByClassName('hamburger')[0];

hamburger.addEventListener('click',()=>{
    navigationBar.classList.toggle('h-resp');
    Array.from(visibilityELement).forEach((element)=>{
        element.classList.toggle('v-resp');
    })
})