<template>
  <VueTinder
    id="tinder-select"
    key-name="id"
    :queue.sync="queue"
    @submit="onSubmit"
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
  props: {
    carMatches,
  },
  data() {
    return {}
  },
  methods: {
    onSubmit(choice) {

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
</style>
