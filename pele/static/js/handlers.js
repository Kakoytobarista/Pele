import {dateField, elementWithTextOfAppointments, fieldDate, selectBody, selectItem} from "./constants.js";
import {getAvailableAppointments} from "./requests.js";


export function addAlert(text) {
    Swal.fire({
        title: text,
        confirmButtonColor: '#944743',
    })
}

function setAttributes(el, attrs) {
    for (let key in attrs) {
        el.setAttribute(key, attrs[key]);
    }
}

function radioCheck() {
    const radioButtons = document.querySelectorAll('.form-check-input');
    for (const radioButton of radioButtons) {
        radioButton.addEventListener("click", () => {
            window.activeAppointment = radioButton.getAttribute("id")
            selectItem.textContent = window.availableAppointments[window.activeAppointment]["time_begin"]
            addAttributeShowToElement(selectBody)
        });
    }
}

export function addAttributeShowToElement(element) {
    element.classList.toggle("show");
    element.classList.toggle("shadow");
}

function delAllValueFromAppointmentElems() {
    Array.from(document.querySelectorAll('.form-check-input, .form-check-label')).forEach(el => el.remove());
}

async function createLabelAndInputElements(element, i) {
    setAttributes(element[i].appendChild(document.createElement("input")),
        {
            "class": "form-check-input", "id": `${i}`,
            "name": "size", "type": "radio", "checked": ""
        })
    setAttributes(element[i].appendChild(document.createElement("label")),
        {"class": "form-check-label", "for": `${i}`})


    let appointmentField = document.querySelectorAll(".form-check-label")
    appointmentField[i].textContent = (await window.timeStart.then((data) => {
                window.availableAppointments = data
                console.log(window.availableAppointments)
                console.log(window.date)
                window.previewAppointment = [`Appointment at DATE: ${data[i]['date']} -- 
                TIME : ${data[i]["time_begin"]} ${data[i]["barber"]}`]
                return window.previewAppointment
            }
        )
    );
}

export async function getAvailableAppointment() {
        const aElementBarber = document.querySelector(".active")
        if (aElementBarber == null){
            addAlert("Fill barber field")
        }
        delAllValueFromAppointmentElems()
         selectItem.textContent = ""
         console.log('change date')

        let date = fieldDate.value
        let barberId = Number(aElementBarber.getAttribute("id_barber"))
        window.timeStart = getAvailableAppointments(date, barberId).then((data) => {
            return data
        })
        for (let i = 0; i < await window.timeStart.then((data => {
            return data.length
        })); i++) {

            await createLabelAndInputElements(elementWithTextOfAppointments, i)
            radioCheck()
        }
}

export async function setFreeAppointmentSpots(func) {
    dateField.addEventListener("change", async () => {
        func()
        }
    )
}

export async function setFreeAppointmentAfterSelectBarber() {

}


export async function isClickToDateField () {
    dateField.addEventListener("click", async () => {
        const aElementBarber = document.querySelector(".active")
        if (aElementBarber == null) {
            addAlert("Set barber name!")
        }
    })
}
