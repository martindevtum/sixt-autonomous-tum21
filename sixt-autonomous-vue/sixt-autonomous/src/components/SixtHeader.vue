<template>
    <div class="header-wrapper">
        <h1 class='sixt-text'> <b> {{ mainHeaderText }} </b> </h1>
        <h4 class='sixt-text'> <b> {{ subHeaderText }} </b> </h4>
    </div>
</template>

<script>
export default {
  name: 'SixtHeader',
  data(){
      return {
          mainHeaderText: 'Sixt autonomous vehicle simulator',
          subHeaderText: 'simulation for autonomous taxis'
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.header-wrapper {
    padding: 1rem;
    margin: 1rem 0rem;
    background-color: #EE7F00;
}
h1 {
  margin: 1rem 0;
}
h4 {
  margin: 1rem 0;
}
.sixt-text {
    color: #ffffff;
}
</style>
