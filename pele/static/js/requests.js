const mainApiUrl = 'http://127.0.0.1/api'
const headersParams = {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        }

export const getAvailableAppointments = async function (date, barberId) {
    try {
        let response = await fetch(`${mainApiUrl}/appointments/get_available_appointment_on_current_day/`, {
                method: 'POST',
                headers: headersParams,
                body: JSON.stringify({
                        'date': date,
                        'barber': barberId
                    }
                )
            }
        )
        return await response.json();
    } catch (e) {
        console.log(e)
    }
}


export const makeRequestToMakeAppointment = async function (name, email,
                                                            phone, comment,
                                                            date, time_begin,
                                                            time_end, id_appointment,
                                                            barber) {
    try {
        let response = await fetch(`${mainApiUrl}/appointments/${id_appointment}/`, {
                method: 'PATCH',
                headers: headersParams,
                body: JSON.stringify({
                    "name": `${name}`,
                    "email": `${email}`,
                    "phone": `${phone}`,
                    "comment": `${comment}`,
                    "date": `${date}`,
                    "time_begin": `${time_begin}`,
                    "time_end": `${time_end}`,
                    "barber": `${barber}`,
                }
                )
            }
        )
        return await response.json();
    } catch (e) {
        console.log(e)
    }
}

export const requestGetBarbers = async function () {
    try {
        let response = await fetch(`${mainApiUrl}/users/get_barbers/`, {
                method: 'GET',
                headers: headersParams,
            }
        )
        return await response.json();
    } catch (e) {
        console.log(e)
    }
}
