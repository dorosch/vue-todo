import Vue from 'vue'

import store from './store/index'
import App from './components/App'


new Vue({
  store,
  render: h => h(App),
}).$mount('#app')
