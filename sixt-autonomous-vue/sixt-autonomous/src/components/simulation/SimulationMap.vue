<template>
    <div class="simulation-map_wrapper">
        <gmap-map
            id="map"
            :zoom="14"    
            :center="center"
        >
        <gmap-marker
            v-for="(m, index) in allVehiclePoints.free"
            :key="`${index}_free`"
            :position="m.position"
            icon="sixt_car.png"                
            @click="center=m.position"
        />
        <gmap-marker
            v-for="(m, index) in allVehiclePoints.blocked"
            :key="`${index}_blocked`"
            :position="m.position"
            icon="sixt_car_reserved.png"                
            @click="center=m.position"
        />
        </gmap-map>
    </div>
</template>

<script>
export default {
  name: 'SimulationMap',
  props: {
    vehicles: Array,
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
      let allVehicles = {
          free: [],
          blocked: [],
      };

      this.vehicles.forEach((vehicle) => {
        if (vehicle.status == 'FREE') {
            allVehicles.free.push(
            {
                position: {
                    lat: vehicle.lat,
                    lng: vehicle.lng,
                }
            });
        } else {
            allVehicles.blocked.push(
            {
                position: {
                    lat: vehicle.lat,
                    lng: vehicle.lng,
                }
            });
        }
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
