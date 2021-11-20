<template>
    <div class="simulation-toolbar-entry-detail__wrapper" > 
        <div class="simulation-toolbar-entry-detail__headline">
            <div class="left-arrow" @click="onDeselectEntry">
                <img src="white-arrow-left.png"> 
            </div>
            <span class="simulation-toolbar-entry-detail__headline--text"> {{this.headline}} </span>
        </div>
        <button type="button">Assign Vehiucle</button>
        <button type="button">Set Passenger Is On</button>
        <button type="button">Set Passenger Is Off</button>
        <button type="button">Set Passenger Is On</button>
        <button type="button">Drive To Destination</button>
        <button type="button">Delete Booking</button>
    </div>

</template>

<script>
export default {
  name: 'SimulationToolbarEntryDetail',
  props: {
    booking: Object,
  },
  mounted() {
      console.log(this.booking);
  },
  computed: {
      headline() {
          return `Booking: ${this.booking.bookingID}`
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
    border-color: #ffffff;
}

.simulation-toolbar-entry-detail__headline--text {
    color: #ffffff;
    font-size: 21px;
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
