<template>
    <div class="simulation-toolbar-entry-detail__wrapper" > 
        <div class="simulation-toolbar-entry-detail__headline">
            <div class="left-arrow" @click="onDeselectEntry">
                <img src="white-arrow-left.png"> 
            </div>
            <span class="simulation-toolbar-entry-detail__headline--text"> {{this.headline}} </span>
        </div>
        <div class="simulation-toolbar-entry-detail__info">
            <div class="simulation-toolbar-entry__wrapper--entry indented"> 
                <span> <b> STATUS: </b> {{this.bookingStatus}}</span>
            </div>
            <div class="simulation-toolbar-entry__wrapper--entry indented"> 
                <span> <b> PICKUP: </b> </span>
                <span>{ long: {{this.bookingStart.long}}, lat: {{this.bookingStart.long}} }</span>
            </div>
            <div class="simulation-toolbar-entry__wrapper--entry indented"> 
                <span> <b> DESTINATION: </b> </span>
                <span>{ long: {{this.bookingEnd.long}}, lat: {{this.bookingEnd.long}} }</span>
            </div>
        </div>
        <div class="simulation-toolbar-entry-detail__buttons">
            <button type="button" :disabled="isDisabledAssignVehicle"> Assign Vehicle </button>
            <button type="button" :disabled="isDisabledPassengerOnButton">Set Passenger Is On</button>
            <button type="button" :disabled="isDisabledPassengerOffButton">Set Passenger Is Off</button>
            <button type="button" :disabled="isDisabledDriveToDest">Drive To Destination</button>
            <button type="button">Delete Booking</button>
        </div>

    </div>

</template>

<script>
export default {
  name: 'SimulationToolbarEntryDetail',
  props: {
    booking: Object,
  },
  computed: {
      headline() {
        return `Booking: ${this.booking.bookingID}`
      },
      isDisabledPassengerOnButton() {
        return !this.booking.vehicleID;
      },
      isDisabledPassengerOffButton() {
        return this.booking.status != 'STARTED';
      },
      isDisabledDriveToDest() {
        return this.booking.status != "STARTED";
      },
      isDisabledAssignVehicle() {
        return !!this.booking.vehicleID;
      },
      bookingStatus() {
          return this.booking.status;
      },
      bookingStart() {
          return {
              long: this.booking.pickupLng,
              lat: this.booking.pickupLat,
          };
      },
      bookingEnd() {
          return {
              long: this.booking.destinationLng,
              lat: this.booking.destinationLat,
          };
      }
  },
  methods: {
      onDeselectEntry() {
          this.$emit('on-deselect-entry');  
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.simulation-toolbar-entry-detail__wrapper {
    display: flex;
    flex-direction: column;
    margin: .5rem;
    padding-left: .5rem;
    max-height: 100%;
    background-color: #2F4858;
    padding-bottom: 1rem;
    border-radius: 5px;
    overflow: scroll;
}

.simulation-toolbar-entry-detail__headline {
    position: relative;
    text-align: center;
    border-bottom-style: dashed;
    padding: .5rem;
    border-width: .5px;
    border-color: #dcdcdc;
}

.simulation-toolbar-entry-detail__headline--text {
    color: #dcdcdc;
    font-size: 21px;
}

.simulation-toolbar-entry-detail__info {
    border-bottom-style: dashed;
    padding: .5rem;
    border-width: .5px;
    border-color: #dcdcdc;
}

button {
    padding: .5rem;
    margin: .5rem;
    cursor: pointer;
}
.left-arrow {
    position: absolute;
    margin: 0;
    height: auto;
    padding-top: .5rem;
    width: 15px;
    height: 15px;
    padding-right: 1rem;
    cursor: pointer;
}
img {
    width: 100%;
    height: 100%;
    object-fit: contain;
}
</style>
