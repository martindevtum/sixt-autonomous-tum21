import Vue from 'vue'
import App from './App.vue'
import * as VueGoogleMaps from "vue2-google-maps"
import config from './../../../sixt-autonomous-microservice/src/config.json';

Vue.config.productionTip = false

Vue.use(VueGoogleMaps, {
  load: {
    key: config.api_key,
    libraries: "places"
  }
});

new Vue({
  render: h => h(App),
}).$mount('#app')
