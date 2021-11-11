import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus'
// import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import 'element-plus/dist/index.css'
// import store from './store'

const app = createApp(App)
app.component('fa', FontAwesomeIcon )
app.use(ElementPlus)
app.use(router).mount('#app')