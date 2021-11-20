<template>
    <div class="simulation-toolbar-entry__wrapper">
        <h1> Booking </h1>
        <div class="simulation-toolbar-entry__wrapper--entry"> 
            <p> ID: {{this.bookingID}}</p>
        </div>
        <div class="simulation-toolbar-entry__wrapper--entry"> 
            <p> STATUS: {{this.bookingStatus}}</p>
        </div>
        <div class="simulation-toolbar-entry__wrapper--entry"> 
            <p> PICKUP: </p>
            <p> long: {{this.bookingStart.long}}</p>
            <p> lat: {{this.bookingStart.long}}</p>
        </div>
        <div class="simulation-toolbar-entry__wrapper--entry"> 
            <p> DESTINATION: </p>
            <p> long: {{this.bookingEnd.long}}</p>
            <p> lat: {{this.bookingEnd.long}}</p>
        </div>
    </div>
</template>

<script>
export default {
  name: 'SimulationToolbarEntry',
  props: {
    booking: Object,
  },
  computed: {
      bookingId() {
          return this.booking.bookingID;
      },
      bookingStatus() {
          return this.booking.bookingStatus;
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
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.simulation-display-entry__wrapper {
    display: flex;
    flex-direction: column;
    padding: 1rem;
    margin: 1rem;
    text-align: left;
    border-width: 2px;
    background-color: #2F4858;
}
.simulation-toolbar-entry__wrapper--entry {
    display: flex;
    flex-direction: column;
}
</style>
