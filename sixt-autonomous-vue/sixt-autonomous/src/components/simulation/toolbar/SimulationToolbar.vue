<template>
    <div 
      class="simulation-toolbar__wrapper"
    >
      <div
        v-if="!this.isEntryDetailView"
        class="simulation-toolbar__entry-list"
      >
        <div
          class="create-booking"
          @click="onCreateBooking"
        >
        </div>
        <SimulationToolbarEntry 
          v-for="booking in allBookings" :key="booking.bookingID"
          :booking="booking"
          @on-entry-selected="onEntrySelected"
        />
      </div>
      <div
        v-else
        class="simulation-toolbar__entry-detail"
      >
        <SimulationToolbarEntryDetail
          :booking="selectedBooking"
          @on-deselect-entry="onDeselectEntry"
        />
      </div>
    </div>
</template>

<script>
import SimulationToolbarEntry from './SimulationToolbarEntry.vue';
import SimulationToolbarEntryDetail from './SimulationToolbarEntryDetail.vue';
export default {
  name: 'SimulationToolbar',
  components: {
    SimulationToolbarEntry,
    SimulationToolbarEntryDetail,
  },
  data() {
    return {
      isEntryDetailView: false,
      selectedBooking: {},
    };
  },
  props: {
    allVehicles: Array,
    allBookings: Array,
  },
  methods: {
    onEntrySelected(selectedEntry) {
      this.selectedBooking = selectedEntry;
      this.isEntryDetailView = true;
    },
    onDeselectEntry() {
      this.selectedBooking = {};
      this.isEntryDetailView = false;
      this.$emit('on-force-refresh');
    },
    onCreateBooking() {

    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.simulation-toolbar__wrapper {
  margin: .5rem;
}
</style>
