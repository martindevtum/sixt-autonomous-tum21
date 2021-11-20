<template>
    <div class="simulation-toolbar-entry__wrapper-container" @click.prevent="onEntrySelected" > 
        <div class="simulation-toolbar-entry__wrapper">
            <h4> <b> Booking </b> </h4>
            <div class="simulation-toolbar-entry__wrapper--entry indented"> 
                <span> <b> ID: </b>  {{this.bookingId}}</span>
            </div>
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
        <div class="right-arrow">
            <img src="white-arrow-right.png"> 
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
  },
  methods: {
      onEntrySelected() {
          this.$emit('on-entry-selected', this.booking);
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.simulation-toolbar-entry__wrapper-container {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin: .5rem;
    padding-left: .5rem;
    max-height: 25%;
    background-color: #2F4858;
    cursor: pointer;
    padding-bottom: 1rem;
    border-radius: 5px;
    overflow: scroll;
}
.simulation-toolbar-entry__wrapper {
    display: flex;
    flex-direction: column;
    text-align: left;
}
.simulation-toolbar-entry__wrapper--entry {
    color: #ffffff;
}
h4 {
    margin: 0.5rem;
}
.indented {
    padding-left: 2rem;
}
.right-arrow {
    padding-top: 4rem;
    width: 25px;
    height: 25px;
    padding-right: 1rem;
}
img {
    width: 100%;
    height: 100%;
    object-fit: contain;
}
</style>
