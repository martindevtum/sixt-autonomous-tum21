<template>
    <div class="simulation-toolbar-entry__wrapper">
        <h4> Booking </h4>
        <div class="simulation-toolbar-entry__wrapper--entry"> 
            <span> ID: {{this.bookingId}}</span>
        </div>
        <div class="simulation-toolbar-entry__wrapper--entry"> 
            <span> STATUS: {{this.bookingStatus}}</span>
        </div>
        <div class="simulation-toolbar-entry__wrapper--entry"> 
            <span> PICKUP: </span>
            <span>{ long: {{this.bookingStart.long}}, lat: {{this.bookingStart.long}} }</span>
        </div>
        <div class="simulation-toolbar-entry__wrapper--entry"> 
            <span> DESTINATION: </span>
            <span>{ long: {{this.bookingEnd.long}}, lat: {{this.bookingEnd.long}} }</span>
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
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.simulation-toolbar-entry__wrapper {
    display: flex;
    flex-direction: column;
    max-height: 25%;
    margin: .5rem;
    padding-left: .5rem;
    text-align: left;
    background-color: #2F4858;
    border-radius: 5px;
    overflow: scroll;
    cursor: pointer;
}
.simulation-toolbar-entry__wrapper--entry {
    color: #ffffff;
}
h4 {
    margin: 0.5rem;
}
</style>
