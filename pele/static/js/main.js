import {getAvailableAppointments, makeRequestToMakeAppointment} from "./requests.js";

const fieldDate = document.getElementById('date')

const selectItem = document.querySelector(".select__output");
const selectBody = document.querySelector(".select__body");
const dateField = document.querySelector("#date");
const elementWithTextOfAppointments = document.querySelectorAll('.select-body__item')


const nameField = document.querySelector("#name")
const emailField = document.querySelector("#email")
const phoneField = document.querySelector("#phone")
const timeField = document.querySelector("#time")
const commentField = document.querySelector("#comment")

const btnSubmit = document.querySelector("#btn_submit")


function addAttributeShowShadow() {
    selectBody.classList.toggle("show");
    selectBody.classList.toggle("shadow");
}

function radioCheck() {
    const radioButtons = document.querySelectorAll('.form-check-input');
    for (const radioButton of radioButtons) {
        radioButton.addEventListener("click", () => {
            window.activeAppointment = radioButton.getAttribute("id")
            selectItem.textContent = window.availableAppointments[window.activeAppointment]["time_begin"]
            addAttributeShowShadow()
        });
    }
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
                window.previewAppointment = [`Appointment at DATE: ${data[i]['date']} -- TIME : ${data[i]["time_begin"]}`]
                return window.previewAppointment
            }
        )
    );
}


function setAttributes(el, attrs) {
    for (let key in attrs) {
        el.setAttribute(key, attrs[key]);
    }
}

function addAlert(text) {
    Swal.fire({
        title: text,
        confirmButtonColor: '#944743',
    })
}

function delAllValueFromAppointmentElems() {
    Array.from(document.querySelectorAll('.form-check-input, .form-check-label')).forEach(el => el.remove());
}

function delValueFromAppointment(id) {
    document.querySelector(`input[id= "${id}"]`).remove()
    document.querySelector(`label[for= "${id}"]`).remove()
    selectItem.textContent = ""
    nameField.textContent = ""
    emailField.textContent = ""
    dateField.textContent = ""
    commentField.textContent = ""


}

async function dropdown() {
    selectItem.addEventListener("click", async () => {

            if (fieldDate.value === '') {
                addAlert("Fill field 'DATE'")
            } else {
                addAttributeShowShadow();
            }
        }
    )
}

async function setFreeAppointmentSpots() {
    dateField.addEventListener("change", async () => {
            delAllValueFromAppointmentElems()
             selectItem.textContent = ""
             console.log('change date')

            let date = fieldDate.value
            window.timeStart = getAvailableAppointments(date).then((data) => {
                return data
            })
            for (let i = 0; i < await window.timeStart.then((data => {
                return data.length
            })); i++) {

                await createLabelAndInputElements(elementWithTextOfAppointments, i)
                radioCheck()
            }
        }
    )
}

async function makeAppointment() {
    await btnSubmit.addEventListener("click", async () => {
            console.log(nameField.value &&
                phoneField.value &&
                timeField.value &&
                dateField.value)
            if (
                nameField.value.length >= 1 &&
                phoneField.value.length >= 1 &&
                timeField.textContent.length >= 1 &&
                dateField.value.length >= 1
            ) {
                let data = window.availableAppointments[window.activeAppointment]
                console.log(window.availableAppointments)
                console.log(data)
                console.log(window.activeAppointment)
                await makeRequestToMakeAppointment(
                    nameField.value,
                    emailField.value,
                    phoneField.value,
                    commentField.value,
                    dateField.value,
                    data["time_begin"],
                    data["time_end"],
                    data["id"])

                delValueFromAppointment(window.activeAppointment)
            }
        }
    )

}


await makeAppointment()
await setFreeAppointmentSpots()
await dropdown()


// LOGIC:
// 1. Dropdown
// 2. Fill data
// 3. Checkbox

