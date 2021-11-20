import Vue from 'vue'
import App from './App.vue'
import * as VueGoogleMaps from "vue2-google-maps" 
import creds from './../../../sixt-autonomous-microservice/src/requests/mapsRequests/creds.json';

Vue.config.productionTip = false

Vue.use(VueGoogleMaps, {
  load: {
    key: creds.api_key,
    libraries: "places"
  }
});

new Vue({
  render: h => h(App),
}).$mount('#app')
