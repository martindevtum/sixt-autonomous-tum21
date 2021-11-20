<template>
    <div class="simulation-toolbar__wrapper">
      <SimulationToolbarEntry 
        v-for="booking in allBookings" :key="booking.bookingID"
        :booking="booking"
      />
    </div>
</template>

<script>
import SimulationToolbarEntry from './SimulationToolbarEntry.vue';
export default {
  name: 'SimulationToolbar',
  components: {
    SimulationToolbarEntry,
  },
  props: {
    allVehicles: Object,
    allBookings: Object,
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.simulation-display__wrapper {

}
</style>
