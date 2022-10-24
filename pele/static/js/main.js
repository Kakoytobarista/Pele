import {getAvailableAppointments} from "./requests.js";

const fieldDate = document.getElementById('date')

const selectItem = document.querySelectorAll(".select__output");
const selectBody = document.querySelectorAll(".select__body");
const elementWithTextOfAppointments = document.querySelectorAll('.select-body__item')



function setAttributes(el, attrs) {
  for(let key in attrs) {
    el.setAttribute(key, attrs[key]);
  }
}

function addAlert(text) {
    Swal.fire({
        title: text,
        confirmButtonColor: '#944743',
    })
}

function delAllValueFromAppointmentElems(){
    Array.from(document.querySelectorAll('.checkbox, .label__checkbox')).forEach(el => el.remove());

}


async function dropdown() {
    selectItem.forEach((item, i) => {
        item.addEventListener("click", async (event) => {
            delAllValueFromAppointmentElems()
            if (fieldDate.value === '') {
                addAlert("Fill field 'DATE'")
            } else if (!selectBody.hasOwnProperty("shadow")){
                selectBody[i].classList.toggle("show");
                item.classList.toggle("shadow");

                let date = fieldDate.value
                window.timeStart = getAvailableAppointments(date).then((data) => {
                    return data
                })
                for (let i = 0; i < await window.timeStart.then((data => {
                    return data.length})); i++) {

                    setAttributes(elementWithTextOfAppointments[i].appendChild(document.createElement("input")),
                        {"type": "checkbox", "class": "checkbox", "id": `checkbox0${i}`})
                    setAttributes(elementWithTextOfAppointments[i].appendChild(document.createElement("label")),
                        {"class": "label__checkbox", "for": `checkbox0${i}`})

                    let appointmentField = document.querySelectorAll(".label__checkbox")
                    appointmentField[i].textContent = (await window.timeStart.then((data) => {
                        let time_start = data[i]['time_begin']
                        let date = data[i]['date']
                        return [time_start, date];
                    }));
                }
            }
        });
    })
}

await dropdown()
