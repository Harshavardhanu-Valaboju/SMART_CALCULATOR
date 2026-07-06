console.log("Smart Vision Calculator Started");

document.querySelectorAll("button").forEach(button=>{

button.addEventListener("mouseenter",()=>{

button.style.boxShadow="0 10px 25px rgba(37,99,235,.25)";

});

button.addEventListener("mouseleave",()=>{

button.style.boxShadow="";

});

});