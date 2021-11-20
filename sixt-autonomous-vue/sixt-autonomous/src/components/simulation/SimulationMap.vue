<template>
    <div class="simulation-map_wrapper">
        <gmap-map
            id="map"
            :zoom="14"    
            :center="center"
        >
            <gmap-marker
                v-for="(m, index) in allVehiclePoints"
                :key="index"
                :position="m.position"
                icon="sixt_car.png"
                @click="center=m.position"
            />
        </gmap-map>
    </div>
</template>

<script>
export default {
  name: 'SimulationMap',
  props: {
    vehicles: Object,
  },
  data() {
    return {
      center: { 
        lat: 48.137154,
        lng: 11.576124,
      },
      existingPlace: null
    };
  },
  computed: {
    allVehiclePoints() {
      const allVehicles = [];
      this.vehicles.forEach((vehicle) => {
        allVehicles.push(
          {
            position: {
                lat: vehicle.lat,
                lng: vehicle.lng,
            }
          }
        );
      });
      console.log(allVehicles);
      return allVehicles;
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #map {
    width: 100%;
    height: 100%;
  }
</style>
