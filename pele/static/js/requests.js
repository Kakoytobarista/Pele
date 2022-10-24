const mainApiUrl = 'http://127.0.0.1:8000/api'
const headersParams = {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        }

export const getAvailableAppointments = async function (date) {
    try {
        let response = await fetch(`${mainApiUrl}/appointments/get_available_appointment_on_current_day/`, {
                method: 'POST',
                headers: headersParams,
                body: JSON.stringify({
                        'date': date
                    }
                )
            }
        )
        return await response.json();
    } catch (e) {
        console.log(e)
    }
}
