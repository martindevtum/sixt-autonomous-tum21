import axios from "axios";
import {
    SIXT_BASE_URL,
} from './../../../config/web-api-config';

const getAllVehicles = async () => {
    return await axios(`${SIXT_BASE_URL}/vehicles`);
};

const getAllBookings = async () => {
    return await axios(`${SIXT_BASE_URL}/bookings`);
};

export {
    getAllVehicles,
    getAllBookings,
};
