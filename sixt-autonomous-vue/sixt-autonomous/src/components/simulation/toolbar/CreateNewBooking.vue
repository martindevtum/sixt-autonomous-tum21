<template>
    <div 
      class="create-new-booking__wrapper"
    >
        <div
            v-if="!isExtended"
            class="create-new-booking__unextended"
            @click="onClick"
        >
            <div class="create-booking__text"> Create Booking </div>
        </div>
        <div
            v-else
            class="create-new-booking__extended"
        >
            <div class="create-new-booking__extended--pickup"> 
                <h4> pickup </h4>
                <p> <span> lat: </span> <input placeholder="set latitude" v-model="pickup_lat"> </p>
                <p> <span> lon: </span> <input placeholder="set longitude" v-model="pickup_long"> </p>
            </div>
            <div class="create-new-booking__destination"> 
                <h4> destination </h4>
                <p> <span> lat: </span> <input placeholder="set latitude" v-model="dest_lat"> </p>
                <p> <span> lon: </span> <input placeholder="set longitude" v-model="dest_long"> </p>
            </div>
            <button type="button" :disabled="!isEnabled" @click="onSubmit"> Submit </button>
        </div>
    </div>
</template>

<script>
import { createBooking } from './../requests/requests';
export default {
  name: 'CreateNewBooking',
  data() {
    return {
      isExtended: false,
      dest_lat: "",
      dest_long: "",
      pickup_lat: "",
      pickup_long: "",
    };
  },
  computed: {
      isEnabled() {
        return !!this.dest_lat.length && !!this.dest_long.length && !!this.pickup_lat.length && !!this.pickup_long.length;
      }
  },
  methods: {
      onClick() {
        this.isExtended = true;
      },
      async onSubmit() {
        await createBooking({ 
            "destinationLat": parseFloat(this.dest_lat),
            "destinationLng": parseFloat(this.dest_long),
            "pickupLat": parseFloat(this.pickup_lat),
            "pickupLng": parseFloat(this.pickup_long),
        })

      this.dest_lat = "";
      this.dest_long = "";
      this.pickup_lat = "";
      this.pickup_long = "";
      this.isExtended = false;
      this.$emit('on-force-refresh');
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.create-new-booking__unextended {
    display: flex;
    flex-direction: row;
    justify-content: center;
    margin: .5rem;
    padding-left: .5rem;
    max-height: 10%;
    background-color: #2F4858;
    cursor: pointer;
    padding-bottom: 1rem;
    border-radius: 5px;
    border-style: dashed;
    border-color:#dcdcdc;
    border-width: 2px;
    overflow: scroll;
}
.create-new-booking__extended {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin: .5rem;
    padding-left: .5rem;
    max-height: 100%;
    background-color: #2F4858;
    padding-bottom: 1rem;
    border-radius: 5px;
}
.create-booking__text {
    color: #dcdcdc;
    padding-top: 1rem;
}
button {
    margin-top: 1rem;
    cursor: pointer;
}
h4 {
    color: #dcdcdc;
}
</style>
