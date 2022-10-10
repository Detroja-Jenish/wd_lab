var countElement = document.getElementById("counter");
let saveElement = document.getElementById("save-entries");

function increase(){
    let count = countElement.innerText;
    count++;
    countElement.innerText = count;
}

function save(){
    saveElement.innerText += " " + countElement.innerText + " -";
    countElement.innerText = 0;
}