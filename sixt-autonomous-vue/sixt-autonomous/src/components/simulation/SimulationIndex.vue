<template>
    <div class="simulation-wrapper">
        <SimulationDisplay 
            class='simulation-display'
            :allVehicles='allVehicles'
            :allBookings='allBookings'
            v-on:refresh-api='refreshApi'
        />
        <SimulationToolbar 
            class='simulation-toolbar'
            :allVehicles='allVehicles'
            :allBookings='allBookings'
            v-on:refresh-api='this.refreshApi'
        />
    </div>
</template>

<script>
import {
    getAllVehicles,
    getAllBookings,
} from './requests/requests';
import SimulationDisplay from './SimulationDisplay.vue';
import SimulationToolbar from './toolbar/SimulationToolbar.vue';
export default {
  name: 'SimulationIndex',
  components: {
      SimulationDisplay,
      SimulationToolbar,
  },
  data() {
      return {
        bookings:[],
        vehicles:[],
      }
  },
  mounted() {
      this.refreshApi();
  },
  methods: {
      refreshApi() {
        this.bookings = getAllBookings(); 
        this.vehicles = getAllVehicles(); 
      },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.simulation-wrapper {
    display: flex;
    position: relative;
    margin: auto;
    margin-top: 1rem;
    margin-bottom: 1rem;
    width: 90%;
    height: 80%;
    background-color: #ffffff;
}
.simulation-display {
    flex-grow: 2;
}
.simulation-toolbar {
    flex-grow: 1;
}
</style>
