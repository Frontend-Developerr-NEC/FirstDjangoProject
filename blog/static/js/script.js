let sideNavbarTogglerOpen = document.getElementById("sideNavbarTogglerOpen");
var sideNavbar = document.getElementById("sideNavbar");
let sideNavbarTogglerClose = document.getElementById("sideNavbarTogglerClose");

sideNavbarTogglerOpen.addEventListener("click",()=>{
sideNavbar.style.display="flex";

})

sideNavbarTogglerClose.addEventListener("click",()=>{
    sideNavbar.style.display="none";

    })