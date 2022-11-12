import {
    dateField,
    elementUlWithTextOfAppointments,
    fieldDate,
    selectBody,
    selectItem, timeField
} from "./constants.js";
import {getAvailableAppointments} from "./requests.js";

export function addAlert(text) {
    Swal.fire({
        title: text,
        confirmButtonColor: '#6c757d',
    })
}

export function addComplete() {
    let timerInterval
    Swal.fire({
        title: '<strong>We make an appointment for you.</strong><br>',
        html: '<br>I will close in <b></b> milliseconds.',
        timer: 2000,
        timerProgressBar: true,
        didOpen: () => {
            console.log("IM here")
            Swal.showLoading()
            const b = Swal.getHtmlContainer().querySelector('b')
            timerInterval = setInterval(() => {
                b.textContent = Swal.getTimerLeft()
            }, 300)
        },
        willClose: () => {
            clearInterval(timerInterval)
        }
    }).then((result) => {
        if (result.dismiss === Swal.DismissReason.timer) {
            console.log('I was closed by the timer')
        }
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
    if (aElementBarber == null) {
        addAlert("Fill barber field")
    }
    delAllValueFromAppointmentElems()
    selectItem.textContent = ""
    timeField.textContent = ""

    let date = fieldDate.value
    let barberId = Number(aElementBarber.getAttribute("id_barber"))
    window.timeStart = getAvailableAppointments(date, barberId).then((data) => {
        return data
    })
    for (let i = 0; i < await window.timeStart.then((data => {
        return data.length
    })); i++) {
        const aElementBarber = document.querySelector(".active")
        if (aElementBarber == null) {
            addAlert("Fill barber field")
        }
        delAllValueFromAppointmentElems()
        selectItem.textContent = ""
        timeField.value = ""

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
}

export async function addEventChange(func, elem) {
    elem.addEventListener("change", async () => {
            timeField.textContent = ""
            func()
        console.log("Change")
        timeField.value = ""
        func()
        }
    )
}

export function changeFunc() {
    document.querySelector('form').submit();
}


export async function isClickToDateField() {
    dateField.addEventListener("click", async () => {
        const aElementBarber = document.querySelector(".active")
        if (aElementBarber == null) {
            addAlert("Choose a barber")
        }
    })
}
