<template>
    <div class="simulation-wrapper">
        <SimulationDisplay 
            class='simulation-display'
            :vehicles='vehicles'
            :bookings='bookings'
            v-on:refresh-api='refreshApi'
            @on-force-refresh="refreshApi"
        />
        <SimulationToolbar 
            class='simulation-toolbar'
            :allVehicles='vehicles'
            :allBookings='bookings'
            v-on:refresh-api='this.refreshApi'
            @on-force-refresh="refreshApi"
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
  async mounted() {
      await this.refreshApi();
  },
  methods: {
      async refreshApi() {
        this.bookings = await getAllBookings(); 
        this.vehicles = await getAllVehicles(); 
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
    margin-bottom: 5rem;
    width: 85%;
    height: 70%;
    max-height: 70vh;
    background-color: #dcdcdc;
}
.simulation-display {
    flex-grow: 3;
    max-height: 100%;
    border-right-style: dotted;
    border-right-width: 2px;
    border-right-color: #EE7F00;
}
.simulation-toolbar {
    flex-grow: 1;
    max-height: 100%;
    overflow: scroll;
}
</style>
