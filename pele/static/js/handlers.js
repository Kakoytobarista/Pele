import {
    dateField,
    elementUlWithTextOfAppointments,
    fieldDate,
    selectBody,
    selectItem
} from "./constants.js";
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
            selectItem.value = window.availableAppointments[window.activeAppointment]["time_begin"]
            addAttributeHideToElement(selectBody)
        });
    }
}

export function addAttributeShowToElement(element) {
    element.style.display = "block";
}

export function addAttributeHideToElement(element) {
   element.style.display = "none";
}

function delAllValueFromAppointmentElems() {
    Array.from(document.querySelectorAll('.form-check-input, ' +
        '.form-check-label, .select-body__item')).forEach(el => el.remove());
}

async function createLabelAndInputElements(element, i) {
    setAttributes(element.appendChild(document.createElement("li")),
        {
            "class": "select-body__item  form-check"
        })
    let liElement = document.querySelectorAll(".select-body__item")
    setAttributes(liElement[i].appendChild(document.createElement("input")),
        {
            "class": "form-check-input", "id": `${i}`,
            "name": "flexRadioDefault", "type": "radio", "checked": ""
        })
    setAttributes(liElement[i].appendChild(document.createElement("label")),
        {"class": "form-check-label", "for": `${i}`})


    let appointmentField = document.querySelectorAll(".form-check-label")
    appointmentField[i].textContent = (await window.timeStart.then((data) => {
                window.availableAppointments = data
                window.previewAppointment = [`Appointment: ${data[i]["time_begin"]} - ${data[i]["time_end"]}`]
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

        let date = fieldDate.value
        let barberId = Number(aElementBarber.getAttribute("id_barber"))
        window.timeStart = getAvailableAppointments(date, barberId).then((data) => {
            return data
        })
        for (let i = 0; i < await window.timeStart.then((data => {
            return data.length
        })); i++) {

            await createLabelAndInputElements(elementUlWithTextOfAppointments, i)
            radioCheck()
        }
}

export async function setFreeAppointmentSpots(func) {
    dateField.addEventListener("change", async () => {
        func()
        }
    )
}


export async function isClickToDateField () {
    dateField.addEventListener("click", async () => {
        const aElementBarber = document.querySelector(".active")
        if (aElementBarber == null) {
            addAlert("Choose a barber")
        }
    })
}
