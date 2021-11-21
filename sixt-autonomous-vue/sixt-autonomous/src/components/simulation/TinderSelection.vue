<template>
  <VueTinder
    id="tinder-select"
    key-name="id"
    :queue.sync="queue"
    @submit="onSubmit"
  >
    <div>
      <img class="profile-pic" :src="currentObj.img">
      <div class="profile-text"> 
          <p> ready in: {{ parseInt(currentObj.vehicle.duration / 60) }} minutes </p>
      </div>
    </div>

    <img slot="like" src="icon_like.png" />
    <img slot="nope" src="icon_dislike.png" />
  </VueTinder>
</template>

<script>
import VueTinder from 'vue-tinder'
import {
  assignVehicleToBooking
} from './requests/requests';
export default {
  components: {
    VueTinder
  },
  data() {
    return {
      currentObj: this.queue[0],
      currentInd: 0,
    };
  },
  props: {
    queue: Array,
    booking: Object,
  },
  methods: {
    onSubmit(choice) {
      if (choice.type == 'nope') {
        if (this.currentInd < this.queue.length - 1) {
          this.currentInd = this.currentInd + 1;
          this.currentObj = this.queue[this.currentInd];
        } else {
          this.endTinder();
        }
      } else if (choice.type == 'like') {
        console.log(this.currentObj);
        this.endTinderSuccess();
      }
    },
    async endTinderSuccess() {
      await assignVehicleToBooking(this.booking.bookingID, this.currentObj.vehicle.vehicleID);
      this.endTinder();
    },
    endTinder() {
      this.$emit('on-force-refresh');
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#tinder-select {
    position: absolute;
    z-index: 10;
    width: 250px;
    height: 400px;
    top: 20%;
}

.profile-pic {
    position: fixed;
    left:0px;
    top: 100px;
    width: 100%;
    height: auto;
}

.profile-text {
  position: fixed;
  bottom: 40px;
  left: 20%;
  color: #000000
}
</style>
