// reference to document controls
const aBox = document.getElementsByTagName("input")[0];
const bBox = document.getElementsByTagName("input")[1];
const btAdd = document.getElementsByTagName("button")[0];
const btSub = document.getElementsByTagName("button")[1];
const btMul = document.getElementsByTagName("button")[2];
const btDiv = document.getElementsByTagName("button")[3];
const btClear = document.getElementsByTagName("button")[4];
const divResult = document.getElementById("divRes");

// 1. Model functions - application logic
function add(a, b) {
    let result = Number(a) + Number(b);
    return result;
}

function sub(a, b) {
    let result = a - b;
    return result;
}

function mul(a, b) {
    return a * b;
}

function div(a, b) {
    return a / b;
}

// 2. View functions - UI - User Interface
function addEvent() {
    let a = aBox.value;
    let b = bBox.value;
    let result = add(a, b);
    divResult.innerHTML = result;
}

function subEvent() {
    let a = aBox.value;
    let b = bBox.value;
    let result = sub(a, b);
    divResult.innerHTML = result;
}

function mulEvent(){
    let a = aBox.value;
    let b = bBox.value;
    let result = mul(a, b);
    divResult.innerHTML = result;
}

function divEvent(){
    let a = aBox.value;
    let b = bBox.value;
    let result = div(a, b);
    divResult.innerHTML = result;
}

function clearUI(){
    divResult.innerHTML = "0";
    aBox.value = "";
    bBox.value = "";
}

// 3. controller - connect button to Event
btAdd.addEventListener("click", addEvent);
btSub.addEventListener("click", subEvent);
btMul.addEventListener("click", mulEvent);
btDiv.addEventListener("click", divEvent);
btClear.addEventListener("click", clearUI);