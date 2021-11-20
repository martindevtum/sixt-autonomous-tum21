<template>
    <div class="simulation-display__wrapper">
      <SimulationMap 
        class='simulation-display__map'
        :vehicles="vehicles"
      />
    </div>
</template>

 
<script>
import SimulationMap from './SimulationMap.vue';

export default {
  name: 'SimulationDisplay',
  components: {
    SimulationMap,
  },
  props: {
    vehicles: Object,
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.simulation-display__wrapper {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 0 1rem;
}
.simulation-display__map {
  width:750px;
  height:450px;
}
</style>
