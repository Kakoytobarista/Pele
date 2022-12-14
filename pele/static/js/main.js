import {makeRequestToMakeAppointment} from "./requests.js";
import {
    fieldDate, selectItem, selectBody, dateField,
    nameField, emailField,
    phoneField, timeField, commentField, btnSubmit
} from "./constants.js"

import {
    addAlert, addAttributeHideToElement,
    addAttributeShowToElement, addComplete, addEventChange,
    getAvailableAppointment,
    isClickToDateField
} from "./handlers.js"


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
            const aElementBarber = document.querySelector(".active")
            if (fieldDate.value === "" || aElementBarber == null) {
                addAlert("Select the date of the appointment to the barber")
            }
            else if (selectBody.style.display === "block") {
                addAttributeHideToElement(selectBody);
            }
            else {
                addAttributeShowToElement(selectBody);
            }
        }
    )
}

async function makeAppointment() {
    await btnSubmit.addEventListener("click", async () => {
        if (
                nameField.value.length >= 1 &&
                phoneField.value.length >= 1 &&
                timeField.value.length >= 1 &&
                dateField.value.length >= 1
            ) {
                addComplete()
                let data = window.availableAppointments[window.activeAppointment]
                let aElementBarber = document.querySelector(".active")
                await makeRequestToMakeAppointment(
                    nameField.value,
                    emailField.value,
                    phoneField.value,
                    commentField.value,
                    dateField.value,
                    data["time_begin"],
                    data["time_end"],
                    data["id"],
                    Number(aElementBarber.getAttribute("id_barber"))
                    )

                delValueFromAppointment(window.activeAppointment)
            }
        }
    )
}


await dropdown()
await makeAppointment()
await addEventChange(getAvailableAppointment, dateField)
await isClickToDateField()



// LOGIC:
// 1. Dropdown
// 2. Fill data
// 3. Checkbox
