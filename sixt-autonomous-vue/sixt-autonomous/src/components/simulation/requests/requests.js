import axios from "axios";
import {
    SIXT_BASE_URL,
} from './../../../config/web-api-config';

const getAllVehicles = async () => {
    return (await axios(`${SIXT_BASE_URL}/vehicles`)).data.allVehicles;
};

const getAllBookings = async () => {
    console.log((await axios(`${SIXT_BASE_URL}/bookings`)).data.allBookings);
    return (await axios(`${SIXT_BASE_URL}/bookings`)).data.allBookings;
};

const deleteBookingById = async (id) => {
    return (await axios.get(`${SIXT_BASE_URL}/bookings/delete/${id}`));
};

const createBooking = async (booking) => {
    return (await axios.post(`${SIXT_BASE_URL}/bookings/create`, booking))
};

const getBestVehicles = async (booking) => {
    const pickupPoint = `${booking.pickupLat},${booking.pickupLng}`;
    return (await axios(`${SIXT_BASE_URL}/bookings/vehicles/${pickupPoint}`)).data.bestVehicles;
};

const passengerGotOn = async (booking) => {
    return (await axios.post(`${SIXT_BASE_URL}/bookings/${booking}/passengerGotOn`))
};

const passengerGotOff = async (booking) => {
    return (await axios.post(`${SIXT_BASE_URL}/bookings/${booking}/passengerGotOff`))
};

const assignVehicleToBooking = async (booking_id, vehicle_id) => {
    console.log(booking_id);
    console.log(vehicle_id);
    return (await axios.post(`${SIXT_BASE_URL}/bookings/${booking_id}/assignVehicle/${vehicle_id}`))
}

export {
    getAllVehicles,
    getAllBookings,
    deleteBookingById,
    createBooking,
    getBestVehicles,
    assignVehicleToBooking,
    passengerGotOff,
    passengerGotOn,
};
