import {requestGetBarbers} from "./requests.js";
import {barberList, barbersElements, dateField, selectBarberField} from "./constants.js"
import {getAvailableAppointment} from "./handlers.js";


async function addBarbersText() {
    window.barbers = requestGetBarbers().then(async (data) => {
        console.log(data)
        console.log(data)
        console.log(data)
        return data
    })
    for (let i = 0; i < await window.barbers.then((data => {
        return data.length
    })); i++) {
        barbersElements[i].textContent = await window.barbers.then((data => {
            barbersElements[i].setAttribute("id_barber", data[i]["id"])
            return `${data[i]["first_name"]} ${data[i]["last_name"]}`
        }))
        barbersElements[i].setAttribute("check", "barber")
    }
}

async function wrapperCheckTimeOut() {
    let td = barberList
    let prev = 0;
    for (let i = 0; i < td.length; i++) {
        td[i].addEventListener('click', function () {
            td[prev].classList.remove('active');
            this.classList.add('active');
            prev = i;
            const aElementBarber = document.querySelector(".active")
            selectBarberField.textContent = `You chose ${aElementBarber.textContent}`
            if (aElementBarber !== null && dateField.value !== ""){
                getAvailableAppointment()
            }
        });
    }
}


await addBarbersText()
await wrapperCheckTimeOut()
