<template>
    <div 
      class="create-new-booking__wrapper"
    >
      <div
        v-if="!isExtended"
        class="create-new-booking__unextended"
      >

      </div>
      <div
        v-else
        class="create-new-booking__extended"
      >
      </div>
    </div>
</template>

<script>
export default {
  name: 'CreateNewBooking',
  data() {
    return {
      isEntryDetailView: false,
      selectedBooking: {},
    };
  },
  methods: {

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.simulation-toolbar__wrapper {
  margin: .5rem;
}
</style>
