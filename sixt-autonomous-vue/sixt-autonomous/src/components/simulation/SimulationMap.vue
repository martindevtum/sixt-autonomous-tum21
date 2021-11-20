<template>
    <div class="simulation-map_wrapper">
        <gmap-map
            id="map"
            :zoom="14"    
            :center="center"
        >
            <gmap-marker
                :key="index"
                v-for="(m, index) in locationMarkers"
                :position="m.position"
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
      locationMarkers: [],
      locPlaces: [],
      existingPlace: null
    };
  },

  computed: {
    getAllVehiclePoints() {
      const allVehicles = [];
      this.vehicles.forEach((vehicle) => {
        allVehicles.push(
          {
            positionString: `q=${vehicle.lat}%2C${vehicle.long}`,
          }
        );
      });
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
