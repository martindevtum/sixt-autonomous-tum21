<template>
  <div id="app">
    <SixtHeader />
    <SimulationIndex />
  </div>
</template>

<script>
import SimulationIndex from './components/simulation/SimulationIndex.vue'
import SixtHeader from './components/SixtHeader.vue'

export default {
  name: 'App',
  components: {
    SimulationIndex,
    SixtHeader,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color:#2F4858;
}
</style>
