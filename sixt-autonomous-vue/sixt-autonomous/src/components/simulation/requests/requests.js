import axios from "axios";
import {
    SIXT_BASE_URL,
} from './../../../config/web-api-config';

const getAllVehicles = async () => {
    return (await axios(`${SIXT_BASE_URL}/vehicles`)).data.allVehicles;
};

const getAllBookings = async () => {
    return (await axios(`${SIXT_BASE_URL}/bookings`)).data.allBookings;
};

const deleteBookingById = async (id) => {
    return (await axios.get(`${SIXT_BASE_URL}/bookings/delete/${id}`));
};

export {
    getAllVehicles,
    getAllBookings,
    deleteBookingById,
};
