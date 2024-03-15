let form = document.getElementById('form')
let button = document.getElementById('button')
function openform() {
    form.classList.add('form-open')
    button.classList.remove('btn-block')
}

function closeform(){
    form.classList.remove('form-open')
    button.classList.add('btn-block')
}

