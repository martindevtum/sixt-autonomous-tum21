<template>
  <VueTinder
    id="tinder-select"
    key-name="id"
    :queue.sync="queue"
  >
    <div
        slot-scope="scope"
        :style="{
            'background-image': `url(https://cn.bing.com//th?id=OHR.${scope.data.id}_UHD.jpg&pid=hp&w=720&h=1280&rs=1&c=4&r=0)`
        }"
    />
    <img slot="like" src="icon_like.png" />
    <img slot="nope" src="icon_dislike.png" />
  </VueTinder>
</template>

<script>
import VueTinder from 'vue-tinder'

export default {
  components: {
    VueTinder
  },
    data() {
        return {
            queue: [{
            // key: 1 （If you do not set the key-name, the 'key' will be used by default. Please ensure that it exists and is independent）
                id: 1
            }, {
                id: 2
            }]
        }
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
</style>
